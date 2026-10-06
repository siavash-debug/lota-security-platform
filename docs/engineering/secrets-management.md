# Secrets Management Policy

This document details how secrets, cryptographic keys, and sensitive credentials are handled in the **LOTA Security Platform**.

---

## 1. Zero Secrets in Source Code

- The codebase is continuously scanned using Gitleaks in CI.
- `.env` files are strictly excluded from source control via `.gitignore`.
- Configuration files accept secrets exclusively through environment variables populated at runtime via HashiCorp Vault or cloud secret managers.

---

## 2. Secrets in Findings and Telemetry

- When scanners discover exposed credentials in customer repositories:
  - The secret value must be hashed or masked before being stored in the database.
  - The API must return only truncated or redacted representations (e.g. `sk_live_...489f`).
  - Evidence files storing secret contexts must be encrypted with tenant-specific keys.
