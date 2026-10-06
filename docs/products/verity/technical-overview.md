# LOTA Security Verity - Technical Overview

> **Authoritative Baseline Reference**: This technical overview is derived from and explicitly references the authoritative [`source-of-truth.md`](file:///docs/products/verity/source-of-truth.md).

---

## 1. Product Mission

**LOTA Security Verity** is an evidence-driven security posture assessment and supply chain analysis platform. It provides security engineers and platform architects with verifiable, repeatable risk evaluations across:

1. **Git Repositories**: Source code posture, commit provenance, branch protections, and CI/CD security.
2. **Software Artifacts & SBOMs**: Pinned dependencies, vulnerability correlation, license compliance, and malicious package signals.
3. **Container Images**: Dockerfile hardening, non-root user verification, layer metadata, and package vulnerabilities.
4. **Security Tool Deployments**: Read-only configuration auditing of defensive platforms (e.g., MISP, Suricata, Zeek).

The platform does **not** certify that software is safe. It produces a repeatable, evidence-backed assessment of known risks, observed capabilities, configuration weaknesses, and analysis limitations.

---

## 2. Core Functional Pipeline

The Verity pipeline progresses through discrete, audited stages:

```text
[Asset Intake] ──> [Immutable Snapshot Resolution] ──> [Worker Job Dispatch]
                                                              │
                                                              ▼
[Findings DB] <── [Evidence Storage] <── [OPA Policy Engine] <── [Normalization]
```

1. **Asset Intake**: Accepts repository URLs, container references, or artifact uploads.
2. **Immutable Snapshot**: Resolves Git refs to commit SHAs and container tags to immutable cryptographic digests.
3. **Scanner Orchestration**: Dispatches tasks to ephemeral, unprivileged worker environments.
4. **Normalization Layer**: Translates disparate scanner and connector outputs into standard domain models.
5. **Policy-as-Code Evaluation**: Evaluates normalized facts against versioned OPA Rego rule bundles.
6. **Evidence Storage**: Preserves cryptographic proof and redacted source snippets for each finding.
7. **Remediation & Exceptions**: Enables expiring policy exceptions and multi-party approval workflows for remediation.
8. **Audit Trail**: Writes immutable audit log entries for all operations.

---

## 3. Analysis Levels

As specified in [`source-of-truth.md`](file:///docs/products/verity/source-of-truth.md#3-supported-analysis-levels):
- **L0 (Metadata Analysis)**: Repository metadata, license, releases, commit history, posture.
- **L1 (Static Repository Analysis)**: Cloned pinned revision; code, manifests, Dockerfiles, IaC, workflows.
- **L2 (Artifact & Image Analysis)**: Container images, packages, binaries, SBOMs, signatures.
- **L3 (Isolated Build Analysis)**: Build in disposable sandbox without credentials (Approval required).
- **L4 (Dynamic Sandbox Analysis)**: Runtime process, network, filesystem telemetry (Approval required).

---

## 4. Architectural Coherence

Refer to the companion technical documents for detailed specifications:
- [Architecture](file:///docs/products/verity/architecture.md)
- [API Contract](file:///docs/products/verity/api-contract.md)
- [Threat Model](file:///docs/products/verity/threat-model.md)
- [Data Model](file:///docs/products/verity/data-model.md)
- [Security Controls](file:///docs/products/verity/security-controls.md)
- [Implementation Roadmap](file:///docs/products/verity/implementation-roadmap.md)
- [Acceptance Criteria](file:///docs/products/verity/acceptance-criteria.md)
- [Limitations](file:///docs/products/verity/limitations.md)
