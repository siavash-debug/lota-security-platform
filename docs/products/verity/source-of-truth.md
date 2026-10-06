# Security Posture Assessment Platform
## Technical Source of Truth

**Document status:** Implementation specification  
**Primary objective:** Build a secure platform that accepts a software source URL, artifact, container image, or SBOM and produces evidence-backed security posture findings, risk assessments, and remediation workflows.

---

## 1. Product Definition

The product is a **Security Posture Assessment and Software Supply Chain Analysis Platform**.

A user submits one of the following:

- Git repository URL, such as GitHub, GitLab, Bitbucket, or self-hosted Git
- Specific Git commit SHA, branch, tag, or release
- Container image reference and immutable image digest
- Release archive, package artifact, binary, or source bundle
- Software Bill of Materials, preferably CycloneDX or SPDX
- Optionally, credentials for a supported security tool integration in read-only mode

The platform analyzes the submitted asset and returns:

- Repository and release provenance information
- Dependency inventory and SBOM
- Known vulnerability exposure
- Secret exposure findings
- Container, Infrastructure-as-Code, CI/CD, and configuration findings
- Dangerous capability map, such as command execution, network access, secret access, privileged container use, or arbitrary tool execution
- Deployment and configuration risks
- Policy compliance results
- Evidence for every finding
- Recommended remediation actions
- Approval-gated remediation workflows where supported

The platform does **not** certify that software is safe. It produces a repeatable, evidence-backed assessment of known risks, observed capabilities, configuration weaknesses, and analysis limitations.

---

## 2. Design Principles

1. **Read-only by default**: Repository inspection, metadata collection, static analysis, and vulnerability analysis must not alter the target repository, deployment, or external systems.
2. **No blind code execution**: Source code, build scripts, Dockerfiles, installation scripts, and downloaded artifacts must not execute on the control plane or developer workstation.
3. **Sandbox-first execution**: Builds and dynamic analysis must run only in disposable, isolated worker environments.
4. **Approval-gated high-risk actions**: Any action that changes infrastructure, access, secrets, networking, policies, or production configuration requires explicit human approval.
5. **Evidence-first findings**: Every finding must contain verifiable evidence, including the source path, line range, AST node, configuration key, API response, scanner result, or artifact hash.
6. **Immutable asset identity**: All analysis results must be pinned to a Git commit SHA, signed release tag and commit SHA, container image digest, artifact SHA-256 digest, or SBOM digest.
7. **Least privilege**: Every connector, worker, service account, API key, and integration must receive only the permissions necessary for its specific function.
8. **Default-deny networking**: Sandboxes and workers should have no outbound network access unless specific destinations are explicitly allowed.
9. **Human-in-the-loop remediation**: The platform may recommend and prepare remediation actions, but high-impact changes must be reviewed and approved by authorized users.
10. **Auditability**: Every important operation must produce an audit event: asset ingestion, scan start, scanner invocation, policy decision, exception, approval, remediation execution, rollback, and failure.

---

## 3. Supported Analysis Levels

| Level | Name | Description | Default State |
|---|---|---|---|
| L0 | Metadata Analysis | Analyze repository metadata, license, contributors, releases, commit history, security policy, archive status, and project posture | Enabled |
| L1 | Static Repository Analysis | Clone a pinned revision and inspect code, manifests, Dockerfiles, CI/CD workflows, IaC, and configuration files | Enabled |
| L2 | Artifact and Image Analysis | Analyze container images, packages, binaries, SBOMs, signatures, provenance, and dependencies | Enabled |
| L3 | Isolated Build Analysis | Build the project in a disposable environment with restricted networking and no sensitive credentials | Disabled unless approved |
| L4 | Dynamic Sandbox Analysis | Run the application and observe process, network, filesystem, API, and runtime behavior | Disabled unless explicitly approved |

### Mandatory restrictions

- L3 and L4 must never run on a developer workstation, production server, shared CI runner, or the platform control plane.
- L3 and L4 environments must not have access to real cloud credentials, SSH keys, browser profiles, production databases, internal DNS zones, Docker sockets, Kubernetes credentials, or mounted host directories.
- Dynamic analysis must have a predefined time limit, resource limit, network policy, and cleanup procedure.

---

## 4. Product Scope

### 4.1 Software Supply Chain Mode

This mode analyzes repositories, packages, artifacts, and container images.

Primary checks include:

- Repository integrity and maintainability
- Commit and release provenance
- Dependency inventory
- SBOM generation
- CVE and vulnerability correlation
- Secret scanning
- Static code analysis
- Dockerfile and container hardening
- Infrastructure-as-Code analysis
- CI/CD workflow analysis
- License and policy compliance
- Dangerous capability extraction
- Runtime behavior analysis in a sandbox, if approved

### 4.2 Security Tool Posture Mode

This mode connects to deployed security tools in read-only mode and evaluates their configuration posture.

Potential integrations include:

- Velociraptor
- osquery
- Sigma repositories and detection pipelines
- YARA rule repositories and scanning pipelines
- Zeek
- Suricata
- MITRE ATT&CK / CTI datasets
- MISP
- TheHive or equivalent case-management systems
- SpiderFoot
- SIEM, ticketing, identity, cloud, and secret-management systems

Primary checks include:

- Public management exposure
- TLS configuration
- SSO and MFA enforcement
- User and role permissions
- API key age, scope, and rotation
- Backup encryption and restore testing
- Audit logging
- Version support lifecycle
- Vulnerability exposure
- Rule and plugin source integrity
- Secret management
- Network egress restrictions
- Configuration drift

---

## 5. Reference Architecture

```text
                         ┌───────────────────────────────┐
                         │       Web UI / Public API      │
                         │ OIDC, MFA, RBAC, Rate Limiting │
                         └───────────────┬───────────────┘
                                         │
                         ┌───────────────▼───────────────┐
                         │     Asset Intake Service       │
                         │ URL validation, snapshotting,  │
                         │ policy selection, ownership   │
                         └───────────────┬───────────────┘
                                         │
                         ┌───────────────▼───────────────┐
                         │ Orchestrator / Workflow Engine │
                         │ Queue, retries, state machine,│
                         │ cancellation, scheduling      │
                         └───────┬─────────┬─────────────┘
                                 │         │
                 ┌───────────────▼───┐ ┌───▼────────────────┐
                 │ Isolated Scan     │ │ Connector Runtime   │
                 │ Workers           │ │ Read-only APIs      │
                 │ Static / Build /  │ │ MISP, Velociraptor, │
                 │ Dynamic Sandbox   │ │ Suricata, etc.      │
                 └───────────────┬───┘ └───┬────────────────┘
                                 │         │
                    ┌────────────▼─────────▼─────────────┐
                    │           Normalization Layer       │
                    │ Common schema for assets, evidence, │
                    │ controls, capabilities, findings    │
                    └────────────┬────────────────────────┘
                                 │
                    ┌────────────▼────────────────────────┐
                    │ Policy Engine                        │
                    │ OPA/Rego or equivalent Policy-as-Code│
                    └────────────┬────────────────────────┘
                                 │
          ┌──────────────────────▼──────────────────────────────┐
          │ Findings Database / Evidence Storage / Audit Ledger  │
          └──────────────────────┬──────────────────────────────┘
                                 │
                    ┌────────────▼────────────────────────┐
                    │ Reporting and Remediation Workflows  │
                    │ Tickets, webhooks, approval, rollback│
                    └─────────────────────────────────────┘
```

---

## 6. Core Services

### 6.1 API Gateway

Responsibilities:

- Authenticate users through OIDC or SAML-backed identity providers
- Require MFA for privileged roles
- Enforce RBAC and, where necessary, attribute-based access control
- Validate repository URLs, artifact references, image names, and user input
- Enforce rate limiting and request size limits
- Prevent SSRF through URL validation and outbound fetch controls
- Assign a `request_id` and `correlation_id` to every request
- Generate audit events for all mutations

The API must not accept arbitrary shell commands, arbitrary network targets, arbitrary local file paths, or arbitrary unrestricted URLs.

### 6.2 Asset Intake Service

Responsibilities:

- Accept Git URLs, artifact references, container image digests, and SBOM uploads
- Normalize and validate source references
- Resolve Git URLs to immutable commit SHAs
- Resolve container tags to immutable digests
- Calculate hashes for uploaded artifacts and SBOMs
- Store source metadata and ownership information
- Select the policy bundle and analysis profile
- Create an immutable scan request

### 6.3 Orchestrator

Responsibilities:

- Create job state machines
- Schedule jobs
- Route jobs to correct workers
- Enforce timeout, retry, concurrency, and budget limits
- Cancel jobs safely
- Preserve idempotency
- Record status transitions
- Ensure a job cannot silently switch from one commit SHA or image digest to another

Suggested job states:

```text
CREATED
VALIDATING
SNAPSHOT_RESOLVED
QUEUED
RUNNING
PARTIAL_SUCCESS
SUCCEEDED
FAILED
CANCELLED
TIMED_OUT
AWAITING_APPROVAL
REMEDIATION_PENDING
REMEDIATION_RUNNING
ROLLED_BACK
```

### 6.4 Isolated Scan Worker

Workers perform static analysis, artifact inspection, builds, and optional dynamic sandbox analysis.

Worker requirements:

- Disposable per job or per tenant
- Non-root process execution
- Read-only root filesystem where possible
- Temporary writable workspace only
- No host filesystem mounts
- No Docker socket mount
- No Kubernetes service account token unless explicitly required
- Drop Linux capabilities
- Apply seccomp and AppArmor or SELinux profiles
- Enforce CPU, memory, storage, process count, and execution time limits
- Use network namespaces
- Default outbound network policy: deny
- Allow only explicitly approved package mirrors, Git hosts, or analysis endpoints
- Destroy worker environment and ephemeral secrets after completion

### 6.5 Connector Runtime

The connector framework integrates with supported products using APIs, configuration exports, logs, or read-only queries.

Connector requirements:

- Read-only by default
- Separate service account and credential for each connector
- Minimal scopes
- Versioned connector contract
- Schema validation for collected data
- Rate limiting and retry policies
- No arbitrary code execution from connector output
- Connector output must be normalized before policy evaluation
- Connector errors must not expose secrets

### 6.6 Policy Engine

The policy engine evaluates normalized facts and produces decisions.

Recommended approach:

- Use Open Policy Agent and Rego
- Store policies in Git
- Require pull request review for policy changes
- Run policy unit tests in CI
- Version policy bundles
- Record the exact policy version used in every scan

Policies must produce:

- `control_id`
- `title`
- `severity`
- `confidence`
- `status`
- `message`
- `evidence_selector`
- `remediation_reference`
- `exception_eligibility`

Policies must not directly execute remediation actions.

### 6.7 Evidence Store

Evidence must be sufficient for a security engineer to verify the finding without rerunning the entire scan.

Evidence examples:

- Repository path and line range
- AST node type and matched rule
- Dockerfile instruction
- Kubernetes manifest field
- Terraform resource configuration
- Dependency name, version, and advisory reference
- Container layer metadata
- API response snapshot with secrets redacted
- TLS handshake details
- User-role assignment
- Configuration hash
- Screenshot or runtime event, if dynamic analysis is enabled

Evidence must be timestamped, hash-addressable, redacted for secrets and unnecessary sensitive data, access controlled, encrypted at rest, and linked to a specific scan and asset snapshot.

### 6.8 Audit Ledger

The platform must record:

- Authentication events
- Asset creation and deletion
- Scan requests
- Policy decisions
- Finding creation, suppression, and closure
- Exception requests and approvals
- Remediation proposals
- Remediation approvals
- Remediation executions
- Rollbacks
- Administrative configuration changes
- Secret access metadata, without logging secret values

Audit logs should be append-only, integrity protected, retained according to policy, and preferably exported to an independent logging system.

---

## 7. Data Model

### 7.1 Asset

```json
{
  "asset_id": "asset_01H...",
  "asset_type": "git_repository",
  "source_url": "https://github.com/example/project",
  "immutable_ref": {
    "commit_sha": "abc123...",
    "branch_at_submission": "main"
  },
  "owner_team": "security-engineering",
  "environment": "assessment",
  "criticality": "high",
  "created_at": "2026-10-05T00:00:00Z"
}
```

### 7.2 Scan

```json
{
  "scan_id": "scan_01H...",
  "asset_id": "asset_01H...",
  "analysis_level": "L1_STATIC",
  "policy_bundle_version": "2026.10.05.1",
  "scanner_versions": {
    "trivy": "x.y.z",
    "semgrep": "x.y.z",
    "gitleaks": "x.y.z"
  },
  "started_at": "2026-10-05T00:00:00Z",
  "ended_at": "2026-10-05T00:10:00Z",
  "status": "SUCCEEDED"
}
```

### 7.3 Finding

```json
{
  "finding_id": "finding_01H...",
  "control_id": "CONTAINER-PRIV-001",
  "title": "Container runs as root",
  "severity": "high",
  "confidence": "high",
  "status": "open",
  "asset_id": "asset_01H...",
  "scan_id": "scan_01H...",
  "evidence_ids": ["evidence_01H..."],
  "remediation": {
    "summary": "Set a non-root USER instruction and configure a non-root security context.",
    "automation_eligible": false
  },
  "first_seen_at": "2026-10-05T00:10:00Z",
  "last_seen_at": "2026-10-05T00:10:00Z"
}
```

### 7.4 Evidence

```json
{
  "evidence_id": "evidence_01H...",
  "scan_id": "scan_01H...",
  "collector": "dockerfile-scanner",
  "location": {
    "path": "Dockerfile",
    "line_start": 12,
    "line_end": 12
  },
  "content_hash": "sha256:...",
  "redacted_payload": {
    "instruction": "USER root"
  },
  "observed_at": "2026-10-05T00:07:00Z"
}
```

### 7.5 Policy Exception

```json
{
  "exception_id": "exception_01H...",
  "control_id": "CONTAINER-PRIV-001",
  "asset_scope": "asset_01H...",
  "justification": "Legacy vendor requirement; migration scheduled.",
  "compensating_controls": [
    "Network isolation",
    "Read-only root filesystem",
    "No host mounts"
  ],
  "approved_by": "user_01H...",
  "expires_at": "2026-11-05T00:00:00Z"
}
```

---

## 8. Static Analysis Pipeline

### 8.1 Repository Snapshot

1. Validate repository URL.
2. Confirm the host is allowed.
3. Resolve the requested branch, tag, or default branch to a commit SHA.
4. Store the commit SHA as the immutable scan reference.
5. Clone only the required revision.
6. Disable Git hooks.
7. Avoid recursive submodule execution by default.
8. Inspect submodules and external references separately.
9. Reject oversized repositories based on configured limits.
10. Record fetch metadata and source hash.

### 8.2 Repository Metadata Analysis

Inspect:

- Repository visibility
- Owner organization or user
- Fork relationship
- Commit activity
- Maintainer activity
- Release cadence
- Archived or abandoned status
- `LICENSE`
- `SECURITY.md`
- `CONTRIBUTING.md`
- Code of conduct
- Signed commits and signed tags
- Branch protection configuration, where available
- Pull request review expectations
- Dependency update automation
- GitHub Actions or equivalent CI workflow security posture
- OpenSSF Scorecard or equivalent project posture data

### 8.3 Manifest and Dependency Analysis

Inspect common dependency definitions:

- `requirements.txt`
- `poetry.lock`
- `Pipfile.lock`
- `package.json`
- `package-lock.json`
- `yarn.lock`
- `pnpm-lock.yaml`
- `go.mod`
- `go.sum`
- `Cargo.toml`
- `Cargo.lock`
- `pom.xml`
- `build.gradle`
- `Gemfile.lock`
- `composer.lock`
- `mix.lock`

Required outputs:

- Dependency graph
- Direct and transitive dependencies
- Exact pinned versions
- Unpinned dependencies
- Vulnerability matches
- Deprecated or unmaintained packages
- Suspicious packages
- Install scripts
- Native binary downloads
- License inventory
- Generated SBOM

### 8.4 Secret Scanning

Detect:

- Cloud access keys
- API keys
- Access tokens
- JWT signing keys
- Private keys
- SSH keys
- Database passwords
- OAuth credentials
- Webhook secrets
- Hard-coded encryption keys
- `.env` files
- Historical secrets in Git history when permitted

Secret scanning must:

- Avoid storing full secret values
- Store masked or hashed representations
- Support verification only through safe, non-destructive methods
- Create remediation guidance for rotation and history cleanup

### 8.5 Docker and Container Analysis

Inspect:

- Base image source
- Pinned digest versus mutable tag
- Use of `latest`
- Root user execution
- `USER` instruction
- `COPY --chown`
- Privileged runtime requirements
- Docker socket mounting
- Host filesystem mounts
- Capabilities
- Exposed ports
- Entrypoint scripts
- Package installation methods
- Downloaded binaries
- `curl | bash`
- Secrets injected at build time
- Multi-stage build usage
- Image size and unnecessary tools
- Known vulnerabilities in OS and language packages

### 8.6 Infrastructure-as-Code Analysis

Support at least:

- Terraform
- Kubernetes manifests
- Helm charts
- Docker Compose
- CloudFormation or equivalent cloud templates

Detect:

- Public ingress
- `0.0.0.0/0` exposure
- Missing TLS
- Privileged containers
- Host networking
- Host PID namespace
- HostPath mounts
- Docker socket mounts
- Running as root
- Missing resource limits
- Secrets in plaintext
- Overly permissive IAM roles
- Public storage buckets
- Missing encryption
- Missing logging
- Insecure security groups
- Excessive egress rules

### 8.7 CI/CD Workflow Analysis

Inspect GitHub Actions, GitLab CI, Jenkinsfiles, and equivalent pipelines.

Detect:

- Unpinned third-party actions
- Mutable action tags
- Secrets exposed to pull requests
- `pull_request_target` misuse
- Shell injection through untrusted input
- Overly broad workflow permissions
- Untrusted artifacts
- Unverified downloads
- Self-hosted runner exposure
- Release publishing without provenance
- Artifact signing gaps

---

## 9. Capability Extraction

The platform must identify what a project is capable of doing, not only whether dependencies have known CVEs.

Capabilities must be mapped to concrete evidence.

### 9.1 High-Risk Capability Categories

| Capability | Examples | Typical Risk |
|---|---|---|
| Shell command execution | `subprocess`, `os.system`, `exec`, `spawn`, shell scripts | High to Critical |
| Dynamic evaluation | `eval`, `exec`, unsafe templating | High |
| Process control | Start, terminate, enumerate processes | High |
| Remote download and execution | Download binary/script and execute | High to Critical |
| Network listeners | HTTP server, TCP listener, RPC endpoint | Medium to Critical |
| Secret access | Environment variables, key stores, credential files | High |
| File system modification | Delete, overwrite, encrypt, chmod | High |
| Docker/Kubernetes control | Docker socket, `kubectl`, Helm, cluster token | Critical |
| Cloud control plane access | AWS/GCP/Azure SDK with admin permissions | Critical |
| Browser automation | Cookies, sessions, browser profiles | Medium to High |
| Data exfiltration | Upload, webhook, remote logging | High |
| LLM tool calling | Agent invokes shell, scanners, external APIs | High to Critical |
| Offensive tooling orchestration | Scanners, fuzzers, exploit frameworks | High to Critical |

### 9.2 Required Evidence Fields

Every extracted capability should include:

```json
{
  "capability_id": "CAP-CMD-EXEC",
  "severity_hint": "critical",
  "source_path": "src/executor.py",
  "line_start": 42,
  "line_end": 49,
  "language": "python",
  "pattern": "subprocess.run(user_input, shell=True)",
  "input_origin": "HTTP request parameter",
  "mitigations_detected": [
    "allowlist: absent",
    "authentication: unknown",
    "authorization: unknown"
  ]
}
```

### 9.3 LLM and Agent-Specific Controls

For AI agents and Model Context Protocol servers, the platform must analyze:

- Whether the LLM can invoke external tools
- Whether tool calls can execute shell commands
- Whether tool arguments come from untrusted user input
- Whether target hostnames, IPs, URLs, file paths, or commands are allowlisted
- Whether the application uses a deterministic validation layer before execution
- Whether agents can access secrets or privileged host resources
- Whether prompt injection could influence tool invocation
- Whether audit logs capture tool calls, parameters, approval state, and output
- Whether the agent can create or terminate processes
- Whether the agent can use offensive security tools
- Whether the agent runs in a disposable, constrained environment

---

## 10. Risk Scoring Model

Risk scoring must not rely only on CVSS or CVEs.

A baseline model is:

\[
Risk = Exposure 	imes Capability 	imes Privilege 	imes SupplyChainUncertainty
\]

Each factor can be scored from 1 to 5.

### 10.1 Exposure

| Score | Meaning |
|---:|---|
| 1 | Offline or local-only |
| 2 | Internal network with strong authentication |
| 3 | Internal network with weak or unknown access controls |
| 4 | Internet reachable with authentication |
| 5 | Internet reachable without effective authentication |

### 10.2 Capability

| Score | Meaning |
|---:|---|
| 1 | Read-only metadata processing |
| 2 | Local data processing |
| 3 | File/network modification |
| 4 | Arbitrary process execution or sensitive data access |
| 5 | Offensive tooling, remote command execution, cloud control, privileged host control |

### 10.3 Privilege

| Score | Meaning |
|---:|---|
| 1 | Unprivileged isolated user |
| 2 | Restricted service account |
| 3 | Elevated local access |
| 4 | Root, broad cloud permissions, or privileged container |
| 5 | Docker socket, cluster-admin, domain admin, or equivalent |

### 10.4 Supply Chain Uncertainty

| Score | Meaning |
|---:|---|
| 1 | Signed release, pinned dependencies, reproducible build |
| 2 | Well-maintained project with lockfiles and provenance |
| 3 | Partial pinning or unclear provenance |
| 4 | Unpinned dependencies, install scripts, unsigned artifacts |
| 5 | Unknown source, suspicious package behavior, unverified binaries |

The final score should be adjusted by:

- Existing authentication
- Network segmentation
- Egress controls
- Compensating controls
- Exploitability
- Data sensitivity
- Presence of active exploitation
- Confidence in the detection
- Policy exceptions

---

## 11. Policy-as-Code Requirements

Policies must be stored in version control and tested in CI.

### 11.1 Policy Rules

Examples:

```rego
package posture

deny[msg] {
  input.asset.type == "misp"
  input.controls.public_admin_exposure == true
  msg := "MISP administrative interface is publicly reachable."
}

deny[msg] {
  input.asset.type == "velociraptor"
  input.controls.mfa_required == false
  msg := "MFA is required for privileged Velociraptor access."
}

warn[msg] {
  input.controls.api_keys_over_90_days > 0
  msg := "One or more API keys exceed the maximum key age."
}

deny[msg] {
  input.container.docker_socket_mounted == true
  msg := "Container mounts the Docker socket."
}

deny[msg] {
  input.container.run_as_root == true
  msg := "Container runs as root."
}
```

### 11.2 Policy Lifecycle

1. Policy author creates a change.
2. CI runs unit tests against compliant and non-compliant fixtures.
3. Reviewer approves the pull request.
4. Policy bundle receives a version.
5. Policy is deployed to staging.
6. Policy is promoted to production.
7. All scan results record the policy bundle version.

### 11.3 Policy Exceptions

Exceptions must contain:

- Control ID
- Asset scope
- Reason
- Business owner
- Security approver
- Compensating controls
- Expiration date
- Renewal workflow
- Audit history

Permanent exceptions should be strongly discouraged.

---

## 12. Remediation Workflow

The platform must separate detection from remediation.

### 12.1 Low-Risk Automation

Can be automated:

- Create a ticket
- Send a webhook
- Notify an owner
- Create a pull request with a proposed configuration change
- Tag an asset
- Open a case in a case-management system
- Request a policy exception review

### 12.2 High-Risk Actions

Must require approval:

- Disabling users
- Revoking API keys
- Changing RBAC
- Changing firewall or security group rules
- Rotating certificates
- Rotating production secrets
- Upgrading core software
- Enabling IPS blocking
- Applying infrastructure changes
- Changing Velociraptor artifacts or osquery packs
- Deleting logs, IOCs, incidents, cases, or attachments

### 12.3 Remediation State Machine

```text
FINDING_OPEN
→ REMEDIATION_PROPOSED
→ OWNER_APPROVED
→ SECURITY_APPROVED
→ CHANGE_WINDOW_APPROVED
→ EXECUTING
→ POST_CHECK_RUNNING
→ COMPLETED

If failure:
EXECUTING
→ FAILED
→ ROLLBACK_RUNNING
→ ROLLED_BACK
→ INCIDENT_OR_TICKET_CREATED
```

Every remediation action must include:

- Fully resolved target
- Exact intended change
- Pre-check
- Post-check
- Rollback plan
- Timeout
- Executor identity
- Approver identity
- Audit record

---

## 13. Security Requirements for the Platform

The platform itself is a high-value target and must be hardened accordingly.

### 13.1 Identity and Access

- Use centralized OIDC or SAML authentication
- Require MFA for privileged users
- Enforce RBAC
- Support separate roles for Viewer, Analyst, Asset Owner, Policy Author, Policy Approver, Remediation Approver, Platform Administrator, and Auditor
- Use short-lived sessions
- Support session revocation
- Require re-authentication for high-risk actions

### 13.2 Secret Management

- Store secrets in Vault, KMS, or a managed secret store
- Do not store raw secrets in source code, logs, findings, database rows, UI, exports, or error messages
- Use short-lived credentials whenever possible
- Rotate connector credentials
- Use separate credentials per integration and per environment
- Record secret access metadata without recording secret values

### 13.3 Sandbox Security

- Use disposable worker environments
- Run as non-root
- Drop capabilities
- Apply seccomp, AppArmor, SELinux, or equivalent isolation
- Enforce read-only root filesystem
- Use ephemeral writable directories
- Disable host mounts
- Disable Docker socket mounts
- Disable privileged mode
- Restrict egress
- Enforce CPU, memory, disk, process, and time quotas
- Destroy the environment after completion
- Destroy temporary credentials after completion

### 13.4 Logging and Monitoring

Log at minimum:

- Login success and failure
- Permission denial
- Scan creation and cancellation
- Worker assignment
- Policy decision
- Secret access metadata
- Exception approval
- Remediation approval
- Remediation execution
- Rollback
- Configuration changes
- Connector failures
- Scanner failures
- Unexpected egress attempts

Logs must:

- Be protected against tampering
- Not contain secrets
- Be retained according to policy
- Be searchable by request ID, asset ID, scan ID, and actor
- Be exported to an independent security monitoring system

---

## 14. Initial Integrations

The first production version should avoid supporting every tool at once.

### 14.1 Recommended MVP Integrations

1. **GitHub or GitLab**
   - Repository metadata
   - Commit and release resolution
   - Security files
   - Workflow inspection
   - Advisory data where available

2. **Container Registry**
   - Image digest resolution
   - Manifest retrieval
   - Layer metadata
   - Signature and provenance checks

3. **MISP Read-Only Connector**
   - User and role posture
   - API key age and scope
   - Organization and sharing configuration
   - Sync peer status
   - Version and lifecycle status
   - Backup signal if exposed safely

4. **Suricata or Zeek Read-Only Connector**
   - Version
   - Config hash
   - Rule source
   - Rule freshness
   - Sensor health
   - Log delivery status
   - Capture interface configuration
   - Drift detection

### 14.2 Later Integrations

- Velociraptor
- osquery fleet management
- SIEM platforms
- Ticketing systems
- Cloud providers
- Identity providers
- Secret managers
- CI/CD systems
- Kubernetes clusters
- TheHive or equivalent incident case management
- SpiderFoot

---

## 15. Recommended Technology Stack

| Layer | Recommended Technology |
|---|---|
| API | FastAPI or Go |
| Worker runtime | Python initially; Go for high-performance workers |
| Database | PostgreSQL |
| Queue | Redis with Celery/RQ, or Temporal for advanced workflows |
| Policy engine | Open Policy Agent with Rego |
| Secrets | HashiCorp Vault, cloud KMS, or managed secret store |
| Object storage | S3-compatible encrypted storage |
| Authentication | Keycloak, Okta, Entra ID, or enterprise OIDC provider |
| UI | React, Next.js, or a minimal server-rendered MVP |
| Logging | OpenSearch, ELK, Loki, or an existing SIEM |
| SBOM | CycloneDX or SPDX |
| Dependency scanning | Trivy, Grype, Dependency-Track |
| Secret scanning | Gitleaks |
| Static analysis | Semgrep and language-specific analyzers |
| IaC scanning | Checkov, Trivy Config, or equivalent |
| Repository posture | OpenSSF Scorecard |
| Container scanning | Trivy, Grype, Syft |
| Deployment | Docker Compose for development; Kubernetes only when justified |

For the MVP, prefer:

```text
FastAPI + PostgreSQL + Redis + Python workers + OPA + Vault + Docker Compose
```

Do not introduce Kubernetes unless multi-tenant isolation, scalable worker scheduling, or enterprise deployment requirements justify the operational complexity.

---

## 16. API Requirements

### 16.1 Create Git Asset

```http
POST /v1/assets/git
```

Request:

```json
{
  "repository_url": "https://github.com/example/project",
  "ref": "main",
  "analysis_profile": "standard-static",
  "owner_team": "security-engineering"
}
```

Response:

```json
{
  "asset_id": "asset_01H...",
  "resolved_commit_sha": "abc123...",
  "status": "snapshot_resolved"
}
```

### 16.2 Create Scan

```http
POST /v1/scans
```

Request:

```json
{
  "asset_id": "asset_01H...",
  "analysis_level": "L1_STATIC",
  "policy_bundle_version": "latest-approved"
}
```

### 16.3 Get Scan Status

```http
GET /v1/scans/{scan_id}
```

### 16.4 Get Findings

```http
GET /v1/findings?asset_id={asset_id}&severity=high,critical
```

### 16.5 Request Exception

```http
POST /v1/exceptions
```

### 16.6 Approve Remediation

```http
POST /v1/remediations/{remediation_id}/approve
```

All state-changing API requests must include:

- Authenticated actor identity
- Authorization check
- Request ID
- Idempotency key
- Audit event
- Input schema validation
- Rate limit enforcement

---

## 17. MVP Acceptance Criteria

The MVP is considered complete only when all of the following are true:

1. A user can submit a Git repository URL.
2. The system resolves and records an immutable commit SHA.
3. The repository is cloned in an isolated worker.
4. Static analysis runs without executing repository code.
5. The platform generates an SBOM.
6. The platform performs dependency vulnerability scanning.
7. The platform performs secret scanning.
8. The platform scans Dockerfiles and IaC files.
9. The platform extracts dangerous capabilities from source and configuration.
10. Findings include severity, confidence, evidence, remediation guidance, and policy version.
11. Findings can be exported as JSON and CSV.
12. Critical and high findings can create webhooks or tickets.
13. Users can create expiring policy exceptions.
14. The platform maintains complete audit logs.
15. Secrets are never visible in logs, reports, UI, or exported findings.
16. Dynamic code execution is disabled by default.
17. No remediation action can run without a recorded approval.
18. The platform can distinguish a failed scan from a completed scan with no findings.
19. The platform documents scan coverage and analysis limitations.
20. The platform supports at least 15 to 25 baseline security controls.

---

## 18. Implementation Roadmap

### Phase 0: Foundation

- Define threat model
- Define data classification
- Define roles and permissions
- Define normalized data model
- Define finding taxonomy
- Define severity and confidence model
- Define policy repository structure
- Define audit event schema

### Phase 1: Repository Intake and Static Analysis

- Git URL intake
- Commit SHA resolution
- Isolated clone
- Repository metadata analysis
- Manifest parsing
- SBOM generation
- Dependency scanning
- Secret scanning
- Findings database
- Evidence storage
- Basic reporting

### Phase 2: Container, IaC, and CI/CD Analysis

- Dockerfile analysis
- Container image scanning
- Kubernetes and Terraform scanning
- GitHub Actions or GitLab CI analysis
- Policy engine integration
- Policy unit tests

### Phase 3: Product Workflow

- Web dashboard
- Asset ownership
- Severity filtering
- Finding lifecycle
- Exceptions
- Webhooks
- Ticket integrations
- Audit dashboard

### Phase 4: Security Tool Connectors

- MISP read-only connector
- Suricata or Zeek read-only connector
- Shared posture controls
- Drift detection
- Configuration evidence collection

### Phase 5: Sandboxed Build and Dynamic Analysis

- Approval-gated L3 build
- Disposable sandbox
- Process/file/network telemetry
- Egress allowlist
- Runtime capability extraction
- Sandbox teardown verification

### Phase 6: Controlled Remediation

- Remediation proposals
- Approval workflow
- Pre-check and post-check
- Rollback implementation
- Change history
- Incident/ticket creation on failure

---

## 19. Explicit Non-Goals

The initial product must not:

- Execute arbitrary user-provided commands
- Run repository code on the platform control plane
- Scan arbitrary internet targets
- Launch exploits against external systems
- Perform credential attacks
- Mount customer host filesystems into scan workers
- Use customer production secrets in dynamic analysis
- Automatically change production security controls without approval
- Claim that a repository is fully secure
- Replace a professional code audit, penetration test, incident response process, or legal authorization process

---

## 20. Definition of Done

A user can submit a repository URL and receive a repeatable assessment bound to an immutable commit SHA.

The assessment includes:

- Source provenance and project posture
- SBOM and dependency inventory
- Vulnerability findings
- Secret findings
- Container, IaC, and CI/CD findings
- Dangerous capability map
- Risk score
- Policy compliance status
- Evidence for every finding
- Remediation recommendations
- Explicit statement of analysis coverage and limitations

The system is secure by design:

- Isolated workers
- Least-privilege credentials
- No secrets in logs
- Policy versioning
- Immutable audit trail
- Approval-gated remediation
- Safe defaults for dynamic analysis and network egress
