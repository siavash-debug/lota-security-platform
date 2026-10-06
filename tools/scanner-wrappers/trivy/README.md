# Trivy Scanner Integration

Wrapper specification for Aqua Security Trivy.

---

## 1. Scope

- Ingests container images, filesystem directories, and IaC manifests.
- Detects OS and language-specific package CVEs, exposed configuration flaws, and license non-compliance.
- Outputs structured JSON conforming to Trivy's v2 schema.
