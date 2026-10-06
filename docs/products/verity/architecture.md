# LOTA Security Verity - System Architecture

> **Authoritative Specification Reference**: This document elaborates on Section 5 ("Reference Architecture") and Section 6 ("Core Services") of [`source-of-truth.md`](file:///docs/products/verity/source-of-truth.md).

---

## 1. Architectural Overview

LOTA Security Verity decouples the control plane from isolated analysis execution workers, ensuring untrusted code never executes within sensitive management zones.

```text
+---------------------------------------------------------------------------------------+
|                                    CONTROL PLANE                                      |
|                                                                                       |
|   +-----------------------+      OIDC / MFA      +--------------------------------+   |
|   |   Verity Web Console  | <------------------> |       Verity API Gateway       |   |
|   +-----------------------+                      +---------------+----------------+   |
|                                                                  |                    |
|                                                                  v                    |
|                                                  +--------------------------------+   |
|                                                  |      Asset Intake Service      |   |
|                                                  +---------------+----------------+   |
|                                                                  |                    |
|                                                                  v                    |
|                                                  +--------------------------------+   |
|                                                  |   Orchestrator / State Machine |   |
|                                                  +---------------+----------------+   |
|                                                                  |                    |
|               +--------------------------------------------------+                    |
|               | State Persistence & Job Queuing                                       |
|               v                                                  v                    |
|   +------------------------------------+         +--------------------------------+   |
|   | PostgreSQL Metadata & Audit Ledger |         |     Redis Job Queue Broker     |   |
|   +------------------------------------+         +---------------+----------------+   |
+------------------------------------------------------------------|--------------------+
                                                                   |
                                    Job Dispatch (Restricted Token)|
                                                                   v
+---------------------------------------------------------------------------------------+
|                                  EXECUTION WORKERS                                    |
|                                                                                       |
|   +------------------------------------+         +--------------------------------+   |
|   |    Isolated Scan Workers (L1/L2)   |         |    Security Connector Runtime  |   |
|   |  - Ephemeral containers            |         |  - Read-only tool APIs         |   |
|   |  - No host mounts / dropped caps   |         |  - Scoped credentials          |   |
|   |  - Egress deny by default          |         |  - MISP, Zeek, Suricata        |   |
|   +-----------------+------------------+         +---------------+----------------+   |
|                     |                                            |                    |
|                     \--------------------\      /----------------/                    |
|                                          v      v                                     |
|                             +----------------------------+                            |
|                             |    Normalization Engine    |                            |
|                             +--------------+-------------+                            |
|                                            | Normalized Facts (JSON)                  |
|                                            v                                          |
|                             +----------------------------+                            |
|                             |      OPA Policy Engine     |                            |
|                             |   (Versioned Rego Bundles) |                            |
|                             +--------------+-------------+                            |
|                                            | Findings & Evidence                      |
|                                            v                                          |
|                             +----------------------------+                            |
|                             | Encrypted Evidence Storage |                            |
|                             |  (MinIO / S3 Object Store) |                            |
|                             +--------------+-------------+                            |
|                                            |                                          |
|                                            v                                          |
|                             +----------------------------+                            |
|                             | Remediation Service (Gate) |                            |
|                             +----------------------------+                            |
+---------------------------------------------------------------------------------------+
```

---

## 2. Core Service Responsibilities

### 2.1 API Gateway
- Authenticates incoming requests via OIDC/SAML; requires MFA for privileged operations.
- Enforces Role-Based Access Control (RBAC).
- Validates URLs and payload schemas; prevents SSRF.
- Generates and injects `request_id` and `correlation_id` into every transaction.
- Emits audit events for all mutating requests.

### 2.2 Asset Intake Service
- Accepts Git URLs, container references, and SBOM files.
- Resolves mutable references to immutable cryptographic digests (commit SHA, image digest).
- Enforces repository size and rate limits.
- Persists asset metadata into PostgreSQL.

### 2.3 Orchestrator
- Manages scan job state machines (`CREATED` -> `VALIDATING` -> `SNAPSHOT_RESOLVED` -> `QUEUED` -> `RUNNING` -> `SUCCEEDED` / `FAILED`).
- Schedules jobs onto Redis worker queues.
- Enforces job timeouts, retry policies, and worker concurrency limits.

### 2.4 Isolated Scan Workers
- Ephemeral worker containers executing unprivileged static analysis tools (Trivy, Semgrep, Gitleaks, Syft).
- Execute with dropped Linux capabilities, read-only root filesystems, and no host filesystem mounts.
- Outbound network access is disabled by default.

### 2.5 Connector Runtime
- Connects in read-only mode to external security tools (GitHub, Container Registry, MISP, Suricata, Zeek).
- Collects configuration and posture data using strictly scoped credentials.

### 2.6 Normalization Layer
- Ingests raw outputs from diverse scanners and connectors.
- Transforms tool-specific outputs into unified domain models (`Finding`, `Evidence`).

### 2.7 OPA Policy Engine
- Evaluates normalized posture facts against declarative Open Policy Agent (OPA) Rego bundles.
- Produces compliance decisions with explicit control IDs, severities, and evidence references.

### 2.8 PostgreSQL Metadata Store
- Stores structured relational data: Assets, Scans, Findings, Policy Exceptions, and Remediation states.

### 2.9 Encrypted Evidence Store (MinIO / S3)
- Stores raw, immutable evidence artifacts, file snippets, and AST nodes.
- Content-addressed via SHA-256 and encrypted at rest with tenant-isolated keys.

### 2.10 Audit Ledger
- Append-only, tamper-evident log recording every scan, policy decision, approval, and configuration change.

### 2.11 Remediation Service
- Manages approval-gated remediation proposals.
- Requires dual authorization (Asset Owner + Security Approver) prior to executing any infrastructure or configuration modification.
