# Verity Contracts & Schemas

This directory houses the formal, versioned API contracts and data schemas governing **LOTA Security Verity**.

---

## 1. Directory Structure

```text
contracts/
├── README.md           # This document
├── openapi/
│   └── openapi.yaml    # OpenAPI 3.1 specification for the Verity REST API
├── events/
│   └── audit-event.schema.json # JSON Schema for immutable audit events
└── models/
    ├── asset.schema.json       # JSON Schema for Asset entity
    ├── scan.schema.json        # JSON Schema for Scan entity
    ├── finding.schema.json     # JSON Schema for Finding entity
    ├── evidence.schema.json    # JSON Schema for Evidence entity
    ├── exception.schema.json   # JSON Schema for PolicyException entity
    └── remediation.schema.json # JSON Schema for RemediationRun entity
```

---

## 2. Validation

All schemas conform to JSON Schema Draft-07 specifications and must contain:
- `$schema`
- `$id`
- `title`
- `description`
- `type`
- `version`

Run contract validation via:
```bash
make contracts-validate
```
