# LOTA Security Verity - Security Controls Catalog

> **Authoritative Specification Reference**: Section 13 ("Security Requirements for the Platform") of [`source-of-truth.md`](file:///docs/products/verity/source-of-truth.md).

---

## 1. Platform Baseline Controls

The following controls are mandated across all Verity deployments:

| Control ID | Category | Name | Description |
|---|---|---|---|
| **CTL-IAM-001** | Identity & Access | OIDC & SAML Federation | Control plane authenticates users via enterprise identity providers. |
| **CTL-IAM-002** | Identity & Access | Mandatory MFA | Multi-Factor Authentication required for all administrative and approval roles. |
| **CTL-IAM-003** | Identity & Access | Role-Based Access Control (RBAC) | Granular roles (Viewer, Analyst, Asset Owner, Approver, Platform Admin). |
| **CTL-IAM-004** | Identity & Access | Scoped Credentials | Tool connectors use discrete, least-privilege tokens scoped to read-only queries. |
| **CTL-CRY-001** | Cryptography | Encryption in Transit | TLS 1.3 enforced on all ingress and internal microservice channels. |
| **CTL-CRY-002** | Cryptography | Encryption at Rest | AES-256 envelope encryption for database volumes and evidence storage buckets. |
| **CTL-SEC-001** | Data Protection | Secret Redaction | Automated redaction filters strip credentials from logs, traces, and finding records. |
| **CTL-AUD-001** | Auditability | Append-Only Audit Ledger | Immutable audit records capturing all mutations, approvals, and scan events. |
| **CTL-WRK-001** | Isolation | Worker Isolation | Ephemeral unprivileged containers (non-root UID, dropped caps, no host mounts). |
| **CTL-NET-001** | Isolation | Egress Deny by Default | Scan workers have zero outbound internet connectivity unless specifically allowlisted. |
| **CTL-INP-001** | Ingress Defense | Schema Validation | Pydantic and JSON Schema validation on all incoming API requests. |
| **CTL-INP-002** | Ingress Defense | SSRF Prevention | Strict URL parsing blocking private, loopback, and cloud metadata IP ranges. |
| **CTL-SCM-001** | Supply Chain | Dependency Pinning | All application dependencies and container base images locked to exact versions/digests. |
| **CTL-SCM-002** | Supply Chain | CycloneDX SBOMs | Automated generation and publication of SBOMs for platform releases. |
| **CTL-SCM-003** | Supply Chain | Signed Provenance | SLSA provenance generation and Cosign image signing on all production images. |
| **CTL-REM-001** | Governance | Remediation Approval Gate | Mandatory dual-authorization checkpoint before executing any remediation. |
