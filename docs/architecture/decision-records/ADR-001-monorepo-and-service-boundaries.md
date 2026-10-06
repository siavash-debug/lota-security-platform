# ADR-001: Monorepo Structure and Service Boundaries

- **Status**: Accepted
- **Date**: 2026-10-05
- **Author**: Principal Software Architect & DevSecOps Lead

---

## 1. Context and Problem Statement

The LOTA Security product suite comprises multiple interrelated cybersecurity products: LOTA Security Verity (evidence-driven security posture assessment), LOTA Security Intelligence (threat intelligence), LOTA Security Response (incident response), and LOTA Security Defense (detection engineering).

These products require shared enterprise primitives—such as secret redaction, audit logging, consistent event models, identity abstractions, and API contract governance—while maintaining strict domain boundaries and independent release lifecycles.

We needed to decide between:
1. Multi-repo approach (independent repositories for each product and library).
2. Monorepo approach (a unified repository housing products, shared platforms, contracts, and documentation).

---

## 2. Decision

We chose to organize the LOTA Security Platform as a **single, structured monorepo** with strict service and directory boundaries:

- `products/`: Isolated product apps, workers, policies, and contracts. Verity is the initial product with implementation scaffolding.
- `shared/`: Common code (`lota_common`), UI component primitives, and common JSON schemas.
- `platform/`: Horizontal enterprise service designs (identity, secrets, audit, observability, workflows).
- `docs/`: Comprehensive technical documentation, architecture specifications, operations runbooks, and ADRs.

---

## 3. Rationale & Consequences

### Advantages
- **Single Source of Truth**: Atomic updates across API contracts, JSON schemas, Rego policies, and service implementations.
- **Unified DevSecOps Governance**: Consistent linting, security scanning, dependency pinning, and PR quality gates across all components.
- **Shared Primitives**: Direct re-use of tested security mechanisms (`lota_common.redaction`, `lota_common.audit`) preventing duplication of critical defensive logic.
- **Clear Product Isolation**: Each product retains its own `apps/`, `policy/`, `connectors/`, and `contracts/` trees, enabling independent packaging and container builds.

### Trade-offs & Mitigations
- *Repository Size*: Mitigated by strict `.gitignore` rules, sparse checkouts in CI where necessary, and prohibition of committed binary artifacts or scan outputs.
- *Blast Radius*: Mitigated by CODEOWNERS, modular test scripts, and isolated worker Dockerfiles.
