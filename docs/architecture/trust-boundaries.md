# Trust Boundaries

This document formalizes the trust boundaries established across the **LOTA Security Platform**.

---

## 1. Trust Boundary Map

```text
+---------------------------------------------------------------------------------------+
|  UNTRUSTED ZONE: Public Internet, External Git Hosts, Malicious Artifacts, Web Clients|
+---------------------------------------------------------------------------------------+
                                           |
                                    [Boundary 1: Ingress Gateway / WAF / OIDC]
                                           v
+---------------------------------------------------------------------------------------+
|  CONTROL PLANE ZONE: Verity API Gateway, Orchestrator, PostgreSQL, OPA, MinIO Storage |
+---------------------------------------------------------------------------------------+
                                           |
                              [Boundary 2: Worker Isolation Barrier]
                                           v
+---------------------------------------------------------------------------------------+
|  ISOLATED WORKER ZONE: Ephemeral Disposable Containers, Read-Only Filesystem, No Sock |
+---------------------------------------------------------------------------------------+
                                           |
                              [Boundary 3: Egress Firewall / Deny Default]
                                           v
+---------------------------------------------------------------------------------------+
|  RESTRICTED EXTERNAL ACCESS: Explicitly Approved Package Mirrors, Read-Only Connectors|
+---------------------------------------------------------------------------------------+
```

---

## 2. Boundary Invariants

### Boundary 1: Ingress & Public API
- Untrusted input is strictly validated using Pydantic models and JSON Schema definitions before reaching internal domain handlers.
- OIDC/SAML authentication verifies caller identity.
- MFA is mandatory for administrative and approval roles.
- Rate limiting protects against denial-of-service abuse.

### Boundary 2: Control Plane vs. Worker Execution
- Workers run in disposable, unprivileged environments.
- Workers receive only the specific inputs required for an assigned job.
- Workers have **no** direct access to the database credentials or master encryption keys.
- Workers output normalized JSON findings and encrypted evidence blobs.

### Boundary 3: Worker Egress
- Default network policy: deny all outbound connections.
- Outbound traffic is restricted to explicitly allowlisted package mirrors or Git remotes during clone phases.
