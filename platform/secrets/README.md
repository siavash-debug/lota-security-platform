# Platform Secrets Management

This subsystem governs cryptographic keys, connector credentials, and runtime secrets across the **LOTA Security Platform**.

---

## 1. Capabilities

- **Vault / Cloud KMS Integration**: Centralized storage and leasing of external connector credentials.
- **Dynamic Secret Leasing**: Short-lived credentials generated on demand for scan workers and connectors.
- **Envelope Encryption**: Data encryption keys (DEKs) wrapped by root key encryption keys (KEKs) per tenant.
- **Automated Rotation**: Continuous auditing and scheduled rotation of long-lived integration credentials.
