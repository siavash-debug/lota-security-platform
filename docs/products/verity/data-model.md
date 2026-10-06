# LOTA Security Verity - Data Model

> **Authoritative Specification Reference**: Section 7 ("Data Model") of [`source-of-truth.md`](file:///docs/products/verity/source-of-truth.md).

---

## 1. Entity Overview

The Verity domain model is structured around seven primary entities:

```text
+-----------+          1:N          +----------+          1:N          +-----------+
|   Asset   | --------------------> |   Scan   | --------------------> |  Finding  |
+-----------+                       +----------+                       +-----+-----+
                                                                             |
                                                                             | M:N
                                                                             v
+-----------------+                 +------------------+               +-----+-----+
| PolicyException |                 |  RemediationRun  |               |  Evidence |
+-----------------+                 +------------------+               +-----------+
         ^                                    ^
         |                                    |
+--------+------------------------------------+------------------------------------+
|                                    AuditEvent                                    |
+----------------------------------------------------------------------------------+
```

---

## 2. Entity Specifications

### 2.1 Asset
Represents a software project, Git repository, container image, or tool deployment under assessment.
- `asset_id`: Prefixed identifier (`asset_01H...`).
- `asset_type`: `git_repository`, `container_image`, `artifact_bundle`, `security_tool`.
- `source_url`: Normalized source location.
- `immutable_ref`: Object containing pinned references (`commit_sha`, `image_digest`).
- `owner_team`: Responsible team identifier.
- `environment`: Deployment stage (`development`, `staging`, `production`, `assessment`).
- `criticality`: Business impact level (`low`, `medium`, `high`, `critical`).
- `created_at`: Creation timestamp.

### 2.2 Scan
Represents an individual assessment execution bound to an asset and analysis level.
- `scan_id`: Prefixed identifier (`scan_01H...`).
- `asset_id`: Associated asset foreign key.
- `analysis_level`: Execution mode (`L0_METADATA`, `L1_STATIC`, `L2_ARTIFACT`, `L3_BUILD`, `L4_DYNAMIC`).
- `policy_bundle_version`: Semantic version or Git hash of active Rego rules.
- `scanner_versions`: Key-value map of scanner tool versions (e.g. `{"trivy": "0.50.0"}`).
- `started_at` / `ended_at`: Timestamps.
- `status`: Execution state (`CREATED`, `QUEUED`, `RUNNING`, `SUCCEEDED`, `FAILED`, `CANCELLED`).

### 2.3 Finding
Represents a specific posture violation, vulnerability, or misconfiguration detected during a scan.
- `finding_id`: Prefixed identifier (`finding_01H...`).
- `control_id`: Policy control code (e.g., `CONTAINER-PRIV-001`, `SECRET-LEAK-001`).
- `title`: Concise finding title.
- `severity`: Standard severity tier (`critical`, `high`, `medium`, `low`, `info`).
- `confidence`: Confidence rating (`high`, `medium`, `low`).
- `status`: Lifecycle state (`open`, `suppressed`, `exception_granted`, `resolved`).
- `asset_id` / `scan_id`: Foreign references.
- `evidence_ids`: Array of associated evidence references.
- `remediation`: Object containing summary instructions and automation eligibility.

### 2.4 Evidence
Immutable, verifiable proof supporting a specific finding.
- `evidence_id`: Prefixed identifier (`evidence_01H...`).
- `scan_id`: Scan during which evidence was gathered.
- `collector`: Originating tool or parser (e.g. `dockerfile-scanner`, `gitleaks`).
- `location`: Structured location (`path`, `line_start`, `line_end`).
- `content_hash`: SHA-256 digest of raw evidence.
- `redacted_payload`: JSON or text excerpt with credentials sanitized.
- `observed_at`: Observation timestamp.

### 2.5 PolicyException
A time-bound, authorized waiver for a specific policy control.
- `exception_id`: Prefixed identifier (`exception_01H...`).
- `control_id`: Targeted control code.
- `asset_scope`: Asset identifier or glob pattern.
- `justification`: Documented business rationale.
- `compensating_controls`: Array of mitigating safeguards.
- `approved_by`: Identity of authorizing security reviewer.
- `expires_at`: Mandatory expiration timestamp.

### 2.6 RemediationRun
Represents the execution lifecycle of a proposed corrective action.
- `remediation_id`: Prefixed identifier (`rem_01H...`).
- `finding_id`: Finding being addressed.
- `action_type`: Remediation action category (e.g., `pr_create`, `config_update`).
- `status`: State machine status (`PROPOSED`, `APPROVED`, `EXECUTING`, `COMPLETED`, `ROLLED_BACK`).
- `approvals`: List of human approvals with reviewer IDs and timestamps.
- `rollback_plan`: Executable rollback specification.

### 2.7 AuditEvent
Immutable record of a state change or privileged action.
- `event_id`: Prefixed identifier (`evt_01H...`).
- `timestamp`: UTC timestamp.
- `actor`: Requestor identity (user, service account, or token ID).
- `action`: Canonical action string.
- `target`: Target entity type and ID.
- `status`: Outcome (`SUCCESS`, `FAILURE`, `DENIED`).
- `metadata`: Sanitized context (IP, request ID, user agent).
