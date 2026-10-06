# LOTA Security Verity

> **Evidence-Driven Security Posture Assessment Platform**

---

## 1. Overview

**LOTA Security Verity** is an evidence-driven security posture assessment platform engineered to ingest:
- Git repository URLs and commit revisions
- Source code archives and release packages
- Container images and immutable digests
- Software Bill of Materials (SBOMs in CycloneDX / SPDX format)
- Security tool configurations in read-only mode

Verity orchestrates static analysis, dependency scanning, secret discovery, Dockerfile/IaC hardening checks, dangerous capability extraction, declarative OPA policy evaluation, and approval-gated remediation.

---

## 2. Directory Layout

```text
products/verity/
├── README.md           # This document
├── apps/
│   ├── api/            # FastAPI control plane gateway
│   ├── worker/         # Isolated scan execution worker runtime
│   └── console/        # Operator web console (Next.js scaffold)
├── policy/
│   ├── bundles/        # Baseline OPA Rego rules and unit tests
│   ├── schemas/        # Policy input schema definitions
│   └── fixtures/       # Compliant and non-compliant test input fixtures
├── connectors/         # Read-only security tool connector adapters
├── contracts/          # OpenAPI 3.1 specifications and JSON Schemas
├── infrastructure/     # Dockerfiles, Compose overrides, K8s manifests
└── scripts/            # Bootstrap, lint, test, and validation scripts
```

---

## 3. Authoritative Specification

The complete, authoritative source of truth for Verity is located at:
[`docs/products/verity/source-of-truth.md`](file:///docs/products/verity/source-of-truth.md)
