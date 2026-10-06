# Data Classification Policy

This document defines the data classification tiers and handling controls applied throughout the **LOTA Security Platform**.

---

## 1. Classification Tiers

| Tier | Category | Examples | Handling Requirements |
|---|---|---|---|
| **Tier 0** | **Public** | Public open-source repository URLs, public CVE advisories, open policy templates. | Plaintext allowed; integrity verification via checksums. |
| **Tier 1** | **Internal Metadata** | Repository names, scan job timestamps, tool execution durations, tenant identifiers. | Encrypted in transit (TLS 1.3); encrypted at rest (AES-256); RBAC required. |
| **Tier 2** | **Confidential Customer Data** | Source code fragments, AST nodes, dependency trees, SBOMs, finding summaries. | Strict tenant isolation; access logging; encrypted at rest; read-only access. |
| **Tier 3** | **Restricted / Sensitive Security Data** | Unmasked secrets discovered in repos, infrastructure credentials, private API keys, vulnerability exploit details. | Mandatory redaction before logging or UI display; zero persistence of raw credentials; hardware-backed KMS/Vault keys. |

---

## 2. Redaction & Sanitization Mandates

- **Secrets Sanitization**: Any secret identified during static analysis must be masked with standard tokenization (e.g., `ghp_************abcd`) or replaced with `[REDACTED]`.
- **Logs & Traces**: Log streams must never ingest request headers containing `Authorization`, `Cookie`, or `X-API-Key`.
- **Evidence Storage**: Evidence blobs containing sensitive source excerpts must be encrypted with tenant-specific envelope encryption keys.
