# Secure Coding Guidelines

All software engineered for the **LOTA Security Platform** must follow these defensive programming standards.

---

## 1. Input Validation & Deserialization

- Validate all inputs using strict Pydantic schemas before processing.
- Reject untrusted URLs containing internal, private, loopback, or metadata addresses (e.g. `169.254.169.254`, `127.0.0.1`, `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`).
- Never use Python `pickle`, `eval()`, or `exec()` for parsing external data.
- Avoid raw shell execution (`shell=True` in `subprocess`).

---

## 2. Secrets Handling

- Never hardcode secrets, passwords, tokens, or encryption keys in source files, fixtures, tests, or documentation.
- Wrap all logging inputs with `lota_common.redaction.redact_sensitive_data()`.
- Filter sensitive HTTP headers (`Authorization`, `Cookie`, `X-Api-Key`) from telemetry and tracing.

---

## 3. Cryptographic Hygiene

- Use modern cryptographic primitives (AES-256-GCM for symmetric encryption, Ed25519 or RSA-4096 for signatures, SHA-256 for hashes).
- Never implement custom cryptographic algorithms.
