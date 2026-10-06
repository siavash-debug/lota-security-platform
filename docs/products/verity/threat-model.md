# LOTA Security Verity - Threat Model

> **Authoritative Specification Reference**: Section 13 ("Security Requirements for the Platform") of [`source-of-truth.md`](file:///docs/products/verity/source-of-truth.md).

---

## 1. Scope & Primary Assets

LOTA Security Verity evaluates potentially hostile code and infrastructure configurations. Its primary assets requiring defense include:
- **Control Plane Integrity**: API gateway, orchestrator, and database.
- **Tenant Isolation**: Protecting one tenant's proprietary code and findings from another.
- **Worker Isolation**: Preventing untrusted repository code from escaping worker containers.
- **Audit Ledger**: Preserving tamper-evident logs of scans, findings, exceptions, and approvals.
- **Connector Secrets**: Read-only API tokens for external security tools and source hosts.

---

## 2. Threat Actors

- **Malicious Repository Submitter**: Submits crafted repositories containing malicious build scripts, submodules, or symlink exploits.
- **Compromised Upstream Connector**: External APIs (e.g. MISP, GitHub) returning malicious or malformed JSON payloads.
- **Untrusted Multi-Tenant User**: Authenticated operator attempting unauthorized privilege escalation or accessing unassigned scans.
- **Hostile Network Observer**: Adversary sniffing internal traffic or attempting SSRF exploitation.

---

## 3. Explicit Abuse Cases & Mitigations

### 3.1 Malicious Repositories & Build-Script Execution
- **Abuse Scenario**: Repository contains weaponized `setup.py`, `package.json` scripts, Git hooks, or Makefile commands designed to execute during checkout.
- **Mitigation**:
  - Clone operations use `git clone --no-checkout` or set `core.hooksPath=/dev/null`.
  - Static analysis tools (L1) parse files as text/AST only; no interpreter is invoked.
  - Workers run as unprivileged users (`UID 10001`).

### 3.2 SSRF Through Repository URLs
- **Abuse Scenario**: User submits `http://169.254.169.254/latest/meta-data/` or internal private IP addresses as a repository URL.
- **Mitigation**:
  - Pre-fetch URL validation parsing scheme, host, and port.
  - DNS resolution check ensuring host does not resolve to loopback (`127.0.0.0/8`), private (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`), or link-local (`169.254.0.0/16`) ranges.
  - Worker network namespace default-deny egress.

### 3.3 Secret Leakage in Findings & Telemetry
- **Abuse Scenario**: Gitleaks finds active production credentials and stores them in plaintext in findings database or logs.
- **Mitigation**:
  - Automatic masking in normalization layer via `lota_common.redaction`.
  - Raw secret values are never displayed in UI, returned via API, or written to logs.

### 3.4 Sandbox Escape
- **Abuse Scenario**: Container breakout vulnerability exploited by a malicious ELF binary or container image layer.
- **Mitigation**:
  - Prohibition of Docker socket mounts (`/var/run/docker.sock`).
  - Read-only container root filesystems with ephemeral `tmpfs` workspaces.
  - Linux capabilities dropped (`CAP_DROP=ALL`).
  - Mandatory seccomp and AppArmor/SELinux profiles.

### 3.5 Connector Credential Compromise
- **Abuse Scenario**: Attacker extracts MISP or Suricata API tokens to execute unauthorized queries.
- **Mitigation**:
  - Connectors are strictly read-only with minimal scopes.
  - Separate service accounts and tokens per integration.
  - Credentials injected dynamically via secret manager; never persisted in worker state.

### 3.6 Policy Tampering
- **Abuse Scenario**: Attacker modifies Rego policy rules to suppress critical findings.
- **Mitigation**:
  - Policies stored in Git as code, requiring PR approval and CI test execution.
  - Scans record the cryptographic hash and version of the policy bundle used.

### 3.7 Unauthorized Remediation
- **Abuse Scenario**: Attacker or automated rule initiates destructive changes (e.g., closing security groups or terminating users) without review.
- **Mitigation**:
  - Complete decoupling of detection from remediation.
  - Dual human approval required (Asset Owner + Security Approver).
  - Remediation actions execute with automated rollback capabilities.

---

## 4. Non-Goals

- Verity does not execute offensive exploits or penetration tests against targets.
- Verity does not perform password guessing or brute-force attacks.
- Verity does not automatically remediate findings without human authorization.
