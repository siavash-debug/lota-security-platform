# Verity Policy-as-Code Subsystem

This directory contains the declarative security posture policies authored in Open Policy Agent (OPA) Rego for **LOTA Security Verity**.

---

## 1. Directory Structure

```text
policy/
├── README.md               # This document
├── bundles/
│   └── baseline/           # Baseline posture policy bundle
│       ├── README.md
│       ├── posture.rego    # Rego policy implementation
│       └── posture_test.rego # Rego unit tests
├── schemas/
│   └── scan-input.schema.json # JSON Schema for normalized scan inputs
└── fixtures/
    ├── compliant/          # Sample inputs that pass all policy checks
    └── noncompliant/       # Sample inputs that trigger expected violations
```

---

## 2. Testing Policies

Execute the local Rego test suite via:
```bash
make policy-test
```
