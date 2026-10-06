# Remediation Approval Framework

The **LOTA Security Platform** strictly segregates detection from remediation.

---

## 1. Approval Workflow

Remediation changes adhere to a finite state machine:

```text
[FINDING_OPEN]
       │
       ▼
[REMEDIATION_PROPOSED] ──> Proposes specific configuration diff or ticket
       │
       ▼
[OWNER_APPROVED]       ──> Resource owner reviews changes
       │
       ▼
[SECURITY_APPROVED]    ──> Security team approves safety & risk
       │
       ▼
[EXECUTING]            ──> Pre-check runs; change applied; post-check runs
       │
       ├─────────────────────────┐
       ▼                         ▼
  [COMPLETED]                 [FAILED] ──> [ROLLBACK_RUNNING] ──> [ROLLED_BACK]
```

---

## 2. Invariants

- **Zero Blind Execution**: No remediation action executes without human sign-off recorded in the audit ledger.
- **Rollback Guarantee**: Every approved automated remediation must provide a tested rollback procedure.
- **Pre & Post Checks**: Automated verification checks run immediately prior to and following execution.
