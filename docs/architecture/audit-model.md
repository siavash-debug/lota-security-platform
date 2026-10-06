# Platform Audit Ledger Model

This document specifies the immutable audit logging architecture for the **LOTA Security Platform**.

---

## 1. Audit Principles

1. **Append-Only Immutability**: Audit events are strictly write-once and can never be modified or deleted through application APIs.
2. **Comprehensive Coverage**: Every state change, authentication event, policy decision, exception approval, and remediation execution must emit an audit event.
3. **Structured Schema**: Audit events conform to a standardized JSON schema (`audit-event.schema.json`).
4. **Secret Sanitization**: Audit payloads record actors, actions, and target metadata, but **never** record unmasked secret values.

---

## 2. Event Structure

Every audit event captures:
- `event_id`: Unique prefixed identifier (e.g. `evt_01H...`).
- `timestamp`: ISO 8601 UTC timestamp.
- `actor`: Identity of the invoking user, service, or API key.
- `action`: Canonical action string (e.g., `asset.create`, `scan.start`, `policy.evaluate`, `exception.approve`, `remediation.execute`).
- `target`: Subject of the action (asset ID, scan ID, exception ID, finding ID).
- `status`: Outcome status (`SUCCESS`, `FAILURE`, `DENIED`).
- `metadata`: Contextual details (IP address, user agent, request ID, correlation ID).
