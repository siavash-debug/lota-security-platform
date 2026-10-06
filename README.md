# LOTA Security Platform

> **Production-Oriented Monorepo Foundation for the LOTA Security Product Suite**

---

## 1. Overview

**LOTA Security** is an enterprise cybersecurity product suite engineered to evaluate, correlate, and harden the security posture of modern software supply chains, cloud environments, and detection operations.

This repository (`lota-security-platform`) is the centralized monorepo hosting the product suite and foundational shared services. It establishes an architectural baseline focused on defensive rigor, strict least privilege, policy-as-code governance, and verifiable auditability.

### The Product Suite

| Product | Focus Area | Status in Monorepo |
|---|---|---|
| **LOTA Security Verity** | Evidence-driven security posture assessment | **Active Initial Scaffolding** |
| **LOTA Security Intelligence** | Threat intelligence and CTI normalization | *Conceptual Architecture (Planned)* |
| **LOTA Security Response** | Incident response and case-management workflows | *Conceptual Architecture (Planned)* |
| **LOTA Security Defense** | Detection engineering and defensive operations | *Conceptual Architecture (Planned)* |

> [!IMPORTANT]
> **Scaffolding Foundation Only**: This repository represents the architectural and engineering foundation. It provides strictly isolated developer tooling, API contracts, domain models, policy bundles, and safe placeholder implementations. It does **not** yet provide live production scanning, dynamic code execution, offensive automation, network penetration capabilities, or automatic production remediation.

---

## 2. LOTA Security Verity

**LOTA Security Verity** is the flagship product included in this initial scaffolding. Verity is an evidence-driven security posture assessment platform that ingests:
- Git repository URLs and commit revisions
- Source artifacts and build packages
- Container images and cryptographically verified digests
- Software Bill of Materials (SBOMs; CycloneDX / SPDX)
- Configuration posture telemetry from supported security integrations (read-only)

### Safe Operational Defaults

Verity enforces security-first invariants across all operations:
1. **Read-Only Analysis**: Source inspection, vulnerability correlation, and posture queries operate in read-only mode by default without modifying target environments.
2. **Immutable Asset Identity**: Every assessment is permanently anchored to an immutable reference (Git commit SHA, container digest, or artifact SHA-256).
3. **Evidence-Backed Findings**: Every finding is accompanied by verifiable, tamper-evident proof (file path, line range, AST node, or raw configuration hash).
4. **Isolated Workers**: Scan engines execute inside disposable worker environments with dropped privileges and no host mounts.
5. **Egress Deny by Default**: Workers have no outbound network connectivity unless specific, cryptographically pinned mirrors are explicitly authorized.
6. **Policy-as-Code**: All evaluations use versioned, declarative Open Policy Agent (OPA) Rego bundles subject to pull request review.
7. **Zero Secrets in Logs**: Structured logs, traces, and finding records strictly redact sensitive tokens, headers, and credentials.
8. **Approval-Gated Remediation**: No corrective mutation or configuration change executes without explicit human authorization.

> [!WARNING]
> **Execution Warning**: Real repository code, build scripts, or unverified container entrypoints must **never** be executed directly by the starter scaffold or control plane.

---

## 3. High-Level Architecture

The following plain text diagram illustrates the control plane and data boundaries across the platform:

```text
+---------------------------------------------------------------------------------------+
|                                    CONTROL PLANE                                      |
|                                                                                       |
|   +-----------------------+      OIDC / MFA      +--------------------------------+   |
|   |   Verity Web Console  | <------------------> |       Verity API Gateway       |   |
|   |   (Operator UI)       |                      | (FastAPI, Schemas, Validation) |   |
|   +-----------------------+                      +---------------+----------------+   |
|                                                                  |                    |
|                                             State / Metadata     v                    |
|                                     +---------------------------------------------+   |
|                                     |    PostgreSQL Metadata & Audit Ledger       |   |
|                                     +---------------------------------------------+   |
|                                                                  |                    |
|                                             Job Scheduling       v                    |
|                                     +---------------------------------------------+   |
|                                     |          Redis Orchestrator Queue           |   |
|                                     +----------------------+----------------------+   |
+------------------------------------------------------------|--------------------------+
                                                             | Secure Job Dispatch
                                                             v
+---------------------------------------------------------------------------------------+
|                                  EXECUTION WORKERS                                    |
|                                                                                       |
|   +------------------------------------+    +-------------------------------------+   |
|   |   Isolated Static Scan Worker      |    |   Security Tool Read-Only Connector |   |
|   |   - Unprivileged Container (No Root|    |   - Scoped Read-Only API Tokens     |   |
|   |   - Ephemeral Workspace            |    |   - Normalized Posture Collector    |   |
|   |   - Egress Deny by Default         |    |   - GitHub, Container Registry,     |   |
|   |   - Trivy, Semgrep, Gitleaks, Syft |    |     MISP, Suricata, Zeek (Planned)  |   |
|   +-----------------+------------------+    +------------------+------------------+   |
|                     |                                          |                      |
|                     \--------------------\  /------------------/                      |
|                                          v  v                                         |
|                             +----------------------------+                            |
|                             |    Normalization Engine    |                            |
|                             +--------------+-------------+                            |
|                                            | Normalized Facts                         |
|                                            v                                          |
|                             +----------------------------+                            |
|                             |      OPA Policy Engine     |                            |
|                             |  (Versioned Rego Bundles)  |                            |
|                             +--------------+-------------+                            |
|                                            | Evidence & Findings                      |
|                                            v                                          |
|                             +----------------------------+                            |
|                             | Encrypted Evidence Storage |                            |
|                             | (MinIO / S3 Object Store)  |                            |
|                             +----------------------------+                            |
+---------------------------------------------------------------------------------------+
```

---

## 4. Local Development Prerequisites

Ensure your workstation has the following tools installed:
- **Git**: 2.40+
- **Python**: 3.12+ (standard development runtime)
- **Node.js**: 20+ LTS (for Verity Console scaffolding)
- **Docker & Docker Compose**: Docker Engine 24+ with Compose V2
- **Make**: Standard GNU Make or compatible build utility
- *(Optional)* **Open Policy Agent (`opa`)**: 0.60+ for local policy validation

---

## 5. Quick-Start Guide

The starter scaffold is configured to run local placeholder services with defensive default settings.

### Step 1: Environment Initialization

Create your local environment files from the provided templates:
```bash
cp .env.example .env
cp compose/dev.env.example compose/dev.env
```

### Step 2: Bootstrap Dependencies

Run the defensive bootstrap script to initialize Python virtual environments:
```bash
make bootstrap
```

### Step 3: Start Local Development Services

Launch the placeholder services using Docker Compose:
```bash
make up
```

This brings up:
- **Verity API** on `http://localhost:8000`
- **PostgreSQL** on `localhost:5432` (development-only credentials)
- **Redis** on `localhost:6379`
- **MinIO** on `localhost:9000` (Console on `localhost:9001`)
- **OPA** on `localhost:8181`

### Step 4: Validate Placeholder Health

Verify that the placeholder API is responding:
```bash
curl -s http://localhost:8000/health
```

Expected output:
```json
{
  "status": "ok",
  "service": "verity-api",
  "environment": "development"
}
```

Check API readiness and version info:
```bash
curl -s http://localhost:8000/ready
curl -s http://localhost:8000/v1/version
```

### Step 5: Shut Down Services

When finished, safely terminate all containers:
```bash
make down
```

---

## 6. Monorepo Organization

```text
lota-security-platform/
├── compose/            # Development environment configurations and secrets templates
├── docs/               # Platform and product architecture, engineering, and ops docs
│   ├── architecture/   # Suite-wide architectural principles, threat models, ADRs
│   ├── engineering/    # Engineering guidelines, testing strategy, secure coding
│   ├── operations/     # Runbooks, observability, incident and disaster recovery
│   ├── policies/       # Policy authoring, exception management, approval gates
│   └── products/       # Deep-dive documentation for Verity, Intelligence, Response, Defense
├── platform/           # Shared platform subsystem specifications (Identity, Secrets, etc.)
├── products/           # Product application implementations
│   └── verity/         # LOTA Security Verity apps, policy, connectors, contracts
├── shared/             # Cross-product shared code, common libraries, schemas, UI tokens
│   └── python/         # lota_common shared Python library
├── tests/              # Multi-component integration, e2e, and security test scaffolds
└── tools/              # Developer scripts and scanner wrappers
```

---

## 7. Authoritative Documentation

The authoritative design and implementation specification for LOTA Security Verity is maintained at:
[`docs/products/verity/source-of-truth.md`](file:///docs/products/verity/source-of-truth.md)

All engineering decisions, data schemas, API contracts, and policy bundles must strictly adhere to that specification.

---

## 8. License & Governance

This project is licensed under the Apache License, Version 2.0. Refer to [LICENSE](file:///LICENSE) and [GOVERNANCE.md](file:///GOVERNANCE.md) for details on contributions and project administration.
