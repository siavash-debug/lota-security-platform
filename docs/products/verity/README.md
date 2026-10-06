# LOTA Security Verity

> **Evidence-Driven Security Posture Assessment Platform**

---

## 1. Authoritative Source of Truth

> [!IMPORTANT]
> **AUTHORITATIVE SPECIFICATION**:  
> The file [`source-of-truth.md`](file:///docs/products/verity/source-of-truth.md) is the **sole authoritative engineering specification** for LOTA Security Verity.  
> It governs all architectural decisions, security boundaries, analysis levels, schemas, workflows, and acceptance criteria.  
> All other documents in this directory are supporting references that break down specific implementation concerns without altering, reinterpreting, or competing with the source of truth.

---

## 2. Product Summary

LOTA Security Verity provides evidence-backed security posture assessments across software supply chains, repository configurations, container images, SBOMs, and connected defensive security tools.

It operates with strict defensive invariants:
- **Read-Only by Default**: No mutation of target repositories or external environments.
- **Immutable Asset Identity**: Pinned to commit SHAs, image digests, or artifact hashes.
- **Isolated Worker Execution**: No code execution on the control plane or developer workstations.
- **Zero Secrets in Logs**: Proactive masking and redaction of credentials.
- **Approval-Gated Remediation**: Separation of detection from mutation.

---

## 3. Supporting Technical Documents

- **[Technical Overview](file:///docs/products/verity/technical-overview.md)**: High-level overview and relationship to the source of truth.
- **[Architecture](file:///docs/products/verity/architecture.md)**: Control plane, workers, normalizer, policy engine, and stores.
- **[API Contract](file:///docs/products/verity/api-contract.md)**: Specifications for initial REST resources and headers.
- **[Threat Model](file:///docs/products/verity/threat-model.md)**: Abuse cases, threat actors, and mitigations.
- **[Data Model](file:///docs/products/verity/data-model.md)**: Core entities: Asset, Scan, Finding, Evidence, Exception, Remediation, Audit.
- **[Security Controls](file:///docs/products/verity/security-controls.md)**: Catalog of platform security controls and safeguards.
- **[Implementation Roadmap](file:///docs/products/verity/implementation-roadmap.md)**: Phases 0 through 6 delivery milestones.
- **[Acceptance Criteria](file:///docs/products/verity/acceptance-criteria.md)**: 20 baseline acceptance criteria derived from the source of truth.
- **[Limitations](file:///docs/products/verity/limitations.md)**: Explicit operational boundaries, false-positive realities, and non-goals.
