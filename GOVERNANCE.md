# Monorepo Governance

The **LOTA Security Platform** is maintained as a multi-product monorepo governed by clear technical decision-making, maintainership roles, and architectural reviews.

---

## 1. Governance Principles

1. **Defensive Rigor**: Every architectural addition must adhere to safe defaults (least privilege, zero secrets in logs, isolated compute, immutable evidence).
2. **Monorepo Ownership**: While shared libraries and platform capabilities reside in common directories, each product team owns its domain apps, contracts, and policies.
3. **Architecture Decision Records (ADRs)**: Any architectural change impacting multiple products or shared boundaries requires an ADR reviewed by the Architecture Working Group.
4. **Policy-as-Code Governance**: Security policies are first-class engineering artifacts stored in version control and tested against compliant/noncompliant fixtures in CI.

---

## 2. Maintainer Roles & Responsibilities

| Role | Scope | Responsibilities |
|---|---|---|
| **Platform Maintainers** | Monorepo root, `platform/`, `shared/`, CI/CD | Oversee core infrastructure, common libraries, security pipelines, repository health. |
| **Product Maintainers** | `products/<product-name>/` | Own product APIs, worker implementations, user interfaces, and domain models. |
| **Security & Policy Approvers** | `products/*/policy/`, `docs/policies/` | Review and sign off on OPA Rego rules, exceptions, and compliance controls. |

---

## 3. Decision-Making Process

- **Standard Features & Bugs**: Managed through Pull Requests requiring at least one approving review from designated CODEOWNERS.
- **Architectural Changes**: Propose an ADR under `docs/architecture/decision-records/` and discuss during architecture review meetings.
- **Security Policy Changes**: Require explicit sign-off from a Security Approver following successful policy unit test execution in CI.
