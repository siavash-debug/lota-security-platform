# LOTA Security Platform Documentation

Welcome to the documentation repository for the **LOTA Security Platform**.

---

## 1. Structure of the Documentation

The documentation is organized into clear functional disciplines:

- **[`architecture/`](file:///docs/architecture/overview.md)**: Platform-wide architectural principles, threat models, trust boundaries, multi-tenancy models, data classification, and Architecture Decision Records (ADRs).
- **[`engineering/`](file:///docs/engineering/local-development.md)**: Engineering practices, testing strategies, coding style guides, dependency management, release procedures, and secure coding standards.
- **[`operations/`](file:///docs/operations/deployment-model.md)**: Infrastructure topology, observability models, backup and restoration, incident response runbooks, and disaster recovery plans.
- **[`policies/`](file:///docs/policies/README.md)**: Policy-as-Code authoring guidelines, exception lifecycle management, and remediation approval gates.
- **[`products/`](file:///docs/products/README.md)**: Product-specific specifications and roadmaps:
  - **[Verity](file:///docs/products/verity/README.md)**: Evidence-driven security posture assessment (Active). Authoritative specification in [`source-of-truth.md`](file:///docs/products/verity/source-of-truth.md).
  - **[Intelligence](file:///docs/products/intelligence/README.md)**: Threat intelligence and CTI platform (Conceptual).
  - **[Response](file:///docs/products/response/README.md)**: Incident response and case management (Conceptual).
  - **[Defense](file:///docs/products/defense/README.md)**: Detection engineering and defense operations (Conceptual).

---

## 2. Documentation Standards

- All documentation is written in English.
- Every architectural decision that crosses service boundaries must be documented in an ADR.
- All technical specifications must align with the security principles detailed in [`architecture/security-principles.md`](file:///docs/architecture/security-principles.md).
