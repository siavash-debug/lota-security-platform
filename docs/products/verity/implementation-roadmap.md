# LOTA Security Verity - Implementation Roadmap

> **Authoritative Specification Reference**: Section 18 ("Implementation Roadmap") of [`source-of-truth.md`](file:///docs/products/verity/source-of-truth.md).

---

## Roadmap Overview

```text
Phase 0 ──> Phase 1 ──> Phase 2 ──> Phase 3 ──> Phase 4 ──> Phase 5 ──> Phase 6
Found.      Static      Containers  Workflow    Connectors  Sandbox     Remediation
```

---

## 1. Phase 0: Foundation (Current Milestone)
- Establish monorepo structure, governance, and DevSecOps tooling.
- Authoritative Verity Source of Truth established.
- Standardize domain models, JSON schemas, and OpenAPI 3.1 contracts.
- Implement `lota_common` shared library (redaction, IDs, error taxonomy, audit).
- Provide safe placeholder implementations for API gateway, worker, and operator console.
- Author baseline OPA Rego policy bundles and test fixtures.
- Provide local development Docker Compose stack.

---

## 2. Phase 1: Repository Intake and Static Analysis
- Git URL intake service with strict SSRF validation.
- Pinned commit SHA resolution.
- Isolated worker cloning mechanism (`--no-checkout` / disabled hooks).
- Repository metadata analysis and OpenSSF Scorecard integration.
- Manifest parsing and CycloneDX/SPDX SBOM generation.
- Dependency vulnerability correlation (Trivy/Grype integration).
- Secret scanning with automated redaction (Gitleaks integration).
- PostgreSQL findings and MinIO encrypted evidence persistence.

---

## 3. Phase 2: Container, IaC, and CI/CD Analysis
- Container image manifest analysis and layer inspection.
- Dockerfile hardening checks (non-root USER, capability drops, socket mounts).
- Infrastructure-as-Code scanning (Terraform, Kubernetes, Helm).
- CI/CD workflow security posture checks (GitHub Actions unpinned actions, `pull_request_target`).
- Full OPA Rego policy engine integration with live evaluation.

---

## 4. Phase 3: Product Workflow
- Production operator web console UI.
- Asset ownership and team assignment.
- Findings lifecycle management (triage, suppression, verification).
- Expiring policy exception request and approval workflows.
- Webhook notifications and ticket synchronizations (Jira, GitHub Issues).
- Audit trail reporting dashboard.

---

## 5. Phase 4: Security Tool Connectors
- Read-only connector for GitHub / GitLab enterprise posture.
- Read-only connector for Container Registries.
- Read-only connector for MISP (API keys, sync peers, user posture).
- Read-only connector for Suricata / Zeek (sensor health, rule freshness, drift).
- Configuration evidence normalization.

---

## 6. Phase 5: Sandboxed Build and Dynamic Analysis
- Approval-gated L3 build analysis in disposable microVMs.
- Runtime process, network, and filesystem telemetry observation (L4).
- Dynamic capability extraction.
- Strict egress allowlisting and automated environment teardown verification.

---

## 7. Phase 6: Controlled Remediation
- Automated remediation proposal generation (PR creation, config updates).
- Multi-party approval state machine (Asset Owner + Security Approver).
- Automated pre-execution and post-execution verification checks.
- Automated rollback engine for failed operations.
