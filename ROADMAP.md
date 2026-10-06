# Product Suite Roadmap

This roadmap outlines the planned evolution of the **LOTA Security Platform** across its foundational milestones and product releases.

---

## Suite-Level Roadmap

```text
[Phase 0: Foundation] ────> [Phase 1: Verity Static MVP] ────> [Phase 2: Verity Containers/IaC]
         │
         ▼
[Phase 3: Verity Workflow & Connectors] ───> [Phase 4: Dynamic Sandbox] ───> [Phase 5: Future Products]
```

---

## 1. Phase 0: Monorepo & Architectural Foundation (Current Milestone)
- [x] Initial monorepo layout and governance structure.
- [x] Baseline architecture, threat models, and security principles.
- [x] Authoritative Verity Source of Truth established.
- [x] API contract, JSON schemas, and OpenAPI 3.1 specifications.
- [x] Safe placeholder FastAPI service with health/readiness endpoints.
- [x] Safe worker and console scaffolds.
- [x] Baseline OPA Rego policy bundles and fixtures.
- [x] Defensive developer tooling (Makefile, bootstrap scripts, linters).
- [x] Development-only Docker Compose environment.

---

## 2. Phase 1: Verity Repository Intake & Static Analysis
- [ ] Git URL intake with strict URL validation and host allowlisting.
- [ ] Immutable commit SHA resolution.
- [ ] Isolated worker clone and workspace sandboxing.
- [ ] Repository metadata inspection and OpenSSF Scorecard correlation.
- [ ] Manifest dependency extraction and CycloneDX SBOM generation.
- [ ] Trivy/Grype vulnerability scanning integration.
- [ ] Gitleaks secret scanning integration with automated redaction.
- [ ] PostgreSQL findings and evidence storage layer.

---

## 3. Phase 2: Verity Container, IaC, and CI/CD Analysis
- [ ] Container image digest resolution and layer inspection.
- [ ] Dockerfile security analysis (root execution, capability checks).
- [ ] Infrastructure-as-Code scanning (Terraform, Kubernetes, Helm).
- [ ] GitHub Actions and CI/CD workflow security posture checks.
- [ ] Automated OPA Rego policy evaluation pipeline.

---

## 4. Phase 3: Verity Workflow, Connectors & Remediation Approvals
- [ ] Next.js operator console UI implementation.
- [ ] Expiring policy exception workflows with audit logging.
- [ ] Read-only connectors for security tools:
  - GitHub / GitLab posture
  - Container Registry posture
  - MISP read-only configuration posture
  - Suricata / Zeek sensor configuration posture
- [ ] Approval-gated remediation state machine (tickets, PR proposals).

---

## 5. Phase 4: Sandboxed Dynamic Analysis (Future)
- [ ] Disposable, microVM/isolated sandbox execution environment.
- [ ] Runtime process, filesystem, and network telemetry observation.
- [ ] Strict default-deny egress network policies.

---

## 6. Phase 5: Suite Expansion (Future Products)
- [ ] **LOTA Security Intelligence**: Threat indicator ingestion, MITRE ATT&CK correlation.
- [ ] **LOTA Security Response**: Case management and incident playbook workflows.
- [ ] **LOTA Security Defense**: Detection rule lifecycle and telemetry posture management.
