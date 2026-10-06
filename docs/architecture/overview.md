# Monorepo Architecture Overview

The **LOTA Security Platform** is a multi-product cybersecurity platform designed around defensive isolation, immutable evidence, and declarative policy governance.

---

## 1. Architectural Model

The platform separates the **Control Plane**, **Execution Workers**, and **External Integrations**:

```text
+-------------------------------------------------------------------------------+
|                                CONTROL PLANE                                  |
|   +-----------------------+                    +--------------------------+   |
|   |    Operator UI / API  | <================> | PostgreSQL & Audit Ledger|   |
|   |    (Authentication,   |                    +--------------------------+   |
|   |     RBAC, Intake)     |                    +--------------------------+   |
|   +-----------+-----------+                    |  Redis Task Orchestrator |   |
|               |                                +-------------+------------+   |
+---------------|----------------------------------------------|----------------+
                |                                              |
                | Job Specification                            | Dispatched Tasks
                v                                              v
+-------------------------------------------------------------------------------+
|                             EXECUTION WORKERS                                 |
|                                                                               |
|   +------------------------------------+    +-----------------------------+   |
|   |     Static Analysis Workers        |    | Security Posture Connectors |   |
|   | (Disposable, Unprivileged, No Host |    | (Read-Only API Collectors,  |   |
|   |  Mounts, Network Deny by Default)  |    |  Zero Execution on Host)    |   |
|   +-----------------+------------------+    +--------------+--------------+   |
|                     |                                      |                  |
|                     \------------------\  /----------------/                  |
|                                        v  v                                   |
|                             +-------------------------+                       |
|                             |  Normalization Layer    |                       |
|                             +------------+------------+                       |
|                                          |                                    |
|                                          v                                    |
|                             +-------------------------+                       |
|                             |    OPA Policy Engine    |                       |
|                             +------------+------------+                       |
|                                          |                                    |
|                                          v                                    |
|                             +-------------------------+                       |
|                             | MinIO Encrypted Evidence|                       |
|                             +-------------------------+                       |
+-------------------------------------------------------------------------------+
```

---

## 2. Platform Core Invariants

1. **Unidirectional Control Flow**: The control plane schedules and delegates tasks to workers. Workers report results back to the normalization layer and object storage.
2. **Immutable References**: Every job is anchored to a cryptographic digest (Git commit SHA, container digest, or artifact SHA-256).
3. **Decoupled Remediation**: Detection never initiates remediation automatically. A remediation engine requires human approval, pre-checks, post-checks, and automatic rollback capabilities.
