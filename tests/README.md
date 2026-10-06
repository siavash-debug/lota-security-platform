# Platform Test Scaffolding

This directory contains integration, end-to-end, security, and fixture test suites for the **LOTA Security Platform**.

---

## 1. Directory Structure

```text
tests/
├── README.md                           # This document
├── integration/                        # Multi-service integration test suites
├── e2e/                                # End-to-end workflow verification tests
├── security/                           # Defensive security tests (isolation, redaction)
└── fixtures/                           # Controlled test fixtures
    ├── safe-repositories/              # Clean benchmark repository fixtures
    ├── intentionally-insecure-repositories/ # Known vulnerable fixtures for rule testing
    └── sample-sboms/                   # Baseline CycloneDX and SPDX SBOM fixtures
```
