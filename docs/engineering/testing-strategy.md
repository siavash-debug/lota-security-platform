# Monorepo Testing Strategy

The **LOTA Security Platform** employs a comprehensive, multi-tiered testing strategy designed to prevent security regressions, ensure contract compliance, and validate policy evaluations.

---

## 1. Test Levels

```text
+-----------------------------------------------------------------+
|   E2E & Security Testing (Isolated sandboxes, auth checks)     |
+-----------------------------------------------------------------+
|   Integration Tests (FastAPI + Postgres + Redis + MinIO mocks)  |
+-----------------------------------------------------------------+
|   Policy Tests (OPA Rego tests against compliant/noncompliant)  |
+-----------------------------------------------------------------+
|   Contract Tests (JSON Schema validation, OpenAPI schema checks)|
+-----------------------------------------------------------------+
|   Unit Tests (FastAPI handlers, lota_common redaction/ID tests) |
+-----------------------------------------------------------------+
```

---

## 2. Test Disciplines

1. **Unit Testing**:
   - `shared/python/lota_common`: Verifies secret redaction, ID generation formats, error taxonomies, and audit event serialization.
   - `products/verity/apps/api`: Tests endpoint schemas, status codes, health routes, and error handlers.
2. **Contract Testing**:
   - Validates that every model under `contracts/models/` and `contracts/events/` matches valid JSON Schema Draft-07 specifications and has required metadata.
3. **Policy-as-Code Testing**:
   - OPA Rego unit tests evaluate static input fixtures under `products/verity/policy/fixtures/compliant/` and `products/verity/policy/fixtures/noncompliant/`.
4. **Security Testing**:
   - Verifies that Authorization headers and secret tokens never leak into structured logs.
   - Ensures workers never run with privileged permissions or host mounts.
