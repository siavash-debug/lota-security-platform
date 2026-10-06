# Shared Platform Subsystems

This directory documents the foundational enterprise subsystems that provide horizontal infrastructure and governance capabilities across the **LOTA Security Platform**.

---

## 1. Platform Subsystems

```text
platform/
├── README.md           # This file
├── identity/           # Centralized identity, OIDC federation, RBAC, and session management
├── secrets/            # Dynamic secrets retrieval, KMS/Vault integration, and key rotation
├── observability/      # OpenTelemetry tracing, Prometheus metrics, and JSON logging
├── audit/              # Append-only audit logging and tamper-evident ledger architecture
└── workflow/           # Distributed job orchestration, queue management, and state machines
```

---

## 2. Cross-Cutting Standards

Each platform subsystem enforces:
- **Zero Static Credentials**: All service-to-service communication relies on mTLS or workload identity.
- **Fail-Closed Security**: In the event of network disruption or policy engine failure, operations default to deny.
- **Standardized Auditability**: All administrative actions produce append-only audit events.
