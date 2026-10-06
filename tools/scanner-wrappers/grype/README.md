# Grype Vulnerability Matcher Integration

Wrapper specification for Anchore Grype.

---

## 1. Scope

- Matches generated SBOM documents and container images against vulnerability databases.
- Identifies CVEs, CVSS scores, fixed versions, and advisory links.
- Operates offline in air-gapped or restricted-network environments using locally synced vulnerability databases.
