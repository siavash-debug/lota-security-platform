# LOTA Security Products

This directory contains product-specific implementations within the **LOTA Security Platform** monorepo.

---

## 1. Product Index

- **[`verity/`](file:///products/verity/README.md)**: **LOTA Security Verity** (Active implementation scaffolding).
- Additional future products (*Intelligence*, *Response*, *Defense*) will be scaffolded in subsequent roadmap phases.

---

## 2. Product Directory Layout

Each product directory maintains strict isolation:
```text
products/<product_name>/
├── README.md
├── apps/               # Executable applications (API gateway, worker, console UI)
├── policy/             # Product-specific OPA Rego policy bundles and test fixtures
├── connectors/         # External tool and platform integration adapters
├── contracts/          # OpenAPI specifications, JSON schemas, event models
├── infrastructure/     # Deployment manifests (Docker, Helm, Compose)
└── scripts/            # Product-specific development and validation scripts
```
