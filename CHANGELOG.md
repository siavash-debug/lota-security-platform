# Changelog

All notable changes to the LOTA Security Platform monorepo are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.1.0] - 2026-10-05

### Added
- Initialized production-oriented monorepo layout for the LOTA Security product suite.
- Established authoritative specification for LOTA Security Verity at `docs/products/verity/source-of-truth.md`.
- Added comprehensive documentation suites across architecture, engineering, operations, and policy governance.
- Added conceptual overview documentation for future products: LOTA Security Intelligence, Response, and Defense.
- Implemented `lota_common` shared Python package with secret redaction, ID generation, custom error taxonomies, and audit models.
- Implemented safe FastAPI application scaffold for LOTA Security Verity with structured JSON logging, Request ID middleware, and safe health endpoints.
- Implemented safe worker execution scaffold with placeholder jobs, scanners, and sandbox modules.
- Implemented Next.js console scaffolding with a clear "Scaffolding Mode" dashboard.
- Implemented baseline OPA/Rego posture policies and unit test fixtures for static input evaluation.
- Added JSON schemas for Asset, Scan, Finding, Evidence, Exception, Remediation, and AuditEvent models.
- Added OpenAPI 3.1 contract specification for Verity REST endpoints.
- Added development-only Docker Compose stack for PostgreSQL, Redis, MinIO, OPA, API, Worker, and Console.
- Added developer tooling: Makefile targets and defensive bash helper scripts.
- Added GitHub governance templates and conservative CI workflows.
