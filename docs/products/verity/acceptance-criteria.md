# LOTA Security Verity - Acceptance Criteria

> **Authoritative Specification Reference**: Section 17 ("MVP Acceptance Criteria") of [`source-of-truth.md`](file:///docs/products/verity/source-of-truth.md).

The Verity MVP is considered complete only when all of the following criteria are demonstrably satisfied:

---

## Acceptance Criteria Matrix

| # | Acceptance Criterion | Verification Method | Status |
|---|---|---|---|
| **AC-01** | A user can submit a Git repository URL via API or Web Console. | Automated contract test for `POST /v1/assets/git`. | Scaffolded (501) |
| **AC-02** | The platform resolves and immutably records the exact Git commit SHA prior to scanning. | Unit test verifying snapshot resolution handler. | Scaffolded |
| **AC-03** | The repository is cloned solely inside an ephemeral, isolated worker container. | Worker environment isolation and non-root audit. | Scaffolded |
| **AC-04** | Static code and manifest analysis executes without running arbitrary repository code. | Worker process execution monitoring audit. | Scaffolded |
| **AC-05** | The platform generates a valid CycloneDX or SPDX Software Bill of Materials (SBOM). | Schema validation of generated SBOM artifact. | Scaffolded |
| **AC-06** | The platform identifies dependency vulnerabilities mapped to known CVE identifiers. | Vulnerability pipeline test against fixture repo. | Scaffolded |
| **AC-07** | The platform executes secret scanning across the repository contents. | Secret scanner test against fixture test files. | Scaffolded |
| **AC-08** | The platform scans Dockerfiles and Infrastructure-as-Code manifests (Terraform/K8s). | IaC scanner test against known misconfigurations. | Scaffolded |
| **AC-09** | The platform extracts dangerous capabilities (e.g. `eval`, `subprocess`, socket access). | Capability extraction test against code samples. | Scaffolded |
| **AC-10** | Every finding includes severity, confidence, cryptographic evidence, and policy version. | Schema validation of finding database records. | Verified in Schema |
| **AC-11** | Findings and evidence can be exported in standardized JSON and CSV formats. | Export API endpoint integration test. | Scaffolded |
| **AC-12** | High and Critical severity findings trigger configured webhook notifications. | Mock webhook listener verification test. | Planned (Phase 3) |
| **AC-13** | Authorized users can request and approve expiring policy exceptions. | Exception lifecycle API test (`POST /v1/exceptions`). | Verified in Schema |
| **AC-14** | Complete, immutable audit log entries are generated for every state change. | Audit table inspection test following operations. | Verified in Schema |
| **AC-15** | Secrets are strictly masked and never appear in raw form in logs, UI, or exports. | Secret hygiene and log parsing test assertion. | Verified in Unit Test |
| **AC-16** | Dynamic execution and runtime analysis are disabled by default. | Configuration flag and pipeline default check. | Enforced by default |
| **AC-17** | No remediation action can execute without recorded multi-party human approval. | State machine test asserting failure without approval. | Scaffolded |
| **AC-18** | The platform reliably distinguishes between a failed scan and a scan with 0 findings. | Scan status transition test suite. | Verified in Contract |
| **AC-19** | The platform explicitly communicates scan coverage boundaries and tool limitations. | Review of generated report metadata. | Documented |
| **AC-20** | The platform enforces at least 15 to 25 baseline security controls via OPA Rego rules. | Rego unit test suite covering baseline controls. | Verified in Rego |
