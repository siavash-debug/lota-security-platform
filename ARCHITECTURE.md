# LOTA Security Architecture Overview

This document describes the architectural layout of the **LOTA Security Platform** monorepo, outlining separation of concerns between shared platform services, common libraries, and independent product applications.

---

## 1. System Philosophy & Layering

The LOTA Security Platform is organized into distinct architectural layers:

```text
+-------------------------------------------------------------------------------+
|                            PRODUCTS LAYER                                     |
|  +--------------------+  +--------------------+  +--------------------+       |
|  |       Verity       |  |    Intelligence    |  |  Response / Defense|       |
|  | (Posture Assessment|  |  (Threat Intel)    |  |  (Incident/Ops)    |       |
|  +----------+---------+  +---------+----------+  +---------+----------+       |
+-------------|----------------------|-----------------------|------------------+
              |                      |                       |
              v                      v                       v
+-------------------------------------------------------------------------------+
|                            PLATFORM LAYER                                     |
|  +--------------------+  +--------------------+  +--------------------+       |
|  | Identity & RBAC    |  | Secrets Management |  | Observability & Trc|       |
|  +--------------------+  +--------------------+  +--------------------+       |
|  +--------------------+  +--------------------+                               |
|  | Immutable Audit    |  | Workflow & Queue   |                               |
|  +--------------------+  +--------------------+                               |
+------------------------------------+------------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------------+
|                          SHARED FOUNDATIONS                                   |
|  +--------------------+  +--------------------+  +--------------------+       |
|  | lota_common (Py)   |  | Shared UI Tokens   |  | JSON Schemas & DTOs|       |
|  | - Redaction        |  | - Reusable Design  |  | - Core Event Models|       |
|  | - Prefixed IDs     |  |   Components       |  | - Common Contracts |       |
|  | - Error Taxonomies |  |                    |  |                    |       |
|  +--------------------+  +--------------------+  +--------------------+       |
+-------------------------------------------------------------------------------+
```

---

## 2. Directory Separation & Boundaries

1. **`products/`**:
   Contains individual, product-specific applications, policies, connectors, and contracts.
   - `products/verity/`: Contains the API gateway, scan worker, operator console, OPA policy bundles, tool connectors, contracts, and deployment infrastructure for Verity.
   - Additional future products (`intelligence/`, `response/`, `defense/`) are documented conceptually and will follow this identical isolation structure.

2. **`platform/`**:
   Houses shared enterprise infrastructure service designs (Identity, Secrets, Observability, Audit, and Workflow). Services here provide horizontal capabilities across products.

3. **`shared/`**:
   Contains language-specific libraries, common schemas, and UI components shared across products.
   - `shared/python/lota_common`: Houses foundational Python primitives (redaction, audit event models, ID generation, error taxonomy).

4. **`docs/`**:
   The comprehensive documentation library covering architecture, engineering practices, operations runbooks, policy authoring guides, and product deep-dives.

---

## 3. Core Architectural Boundaries

- **Strict Worker Isolation**: Workers executing analysis operate in ephemeral, unprivileged environments without access to control plane credentials or host filesystems.
- **Contract-First Communication**: All inter-service and client-server communication is governed by versioned OpenAPI specifications and JSON Schemas located under `contracts/`.
- **Decoupled Remediation**: Detection and analysis logic never triggers active remediation directly. Remediation runs as a discrete, approval-gated state machine.
