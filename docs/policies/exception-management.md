# Policy Exception Management

Security controls are vital, but operational reality occasionally requires temporary exceptions. The **LOTA Security Platform** enforces a rigorous exception governance model.

---

## 1. Exception Principles

1. **Expiring by Default**: Permanent exceptions are forbidden. The maximum lifespan of any exception is 90 days.
2. **Compensating Controls Required**: Every exception must state verified compensating controls mitigating the risk.
3. **Dual Approval**: High-severity control exceptions require approval from both the Asset Owner and a Security Approver.
4. **Audit Trail**: Requesting, approving, renewing, or revoking an exception generates an append-only audit event.

---

## 2. Exception Schema Reference

Exceptions conform to `exception.schema.json`:
- `control_id`: Target policy control ID (e.g. `CONTAINER-PRIV-001`).
- `asset_scope`: Specific asset or repository ID.
- `justification`: Detailed business and technical rationale.
- `compensating_controls`: Array of compensating controls active during the exception.
- `approved_by`: Identity of the authorizing security engineer.
- `expires_at`: ISO 8601 expiration timestamp.
