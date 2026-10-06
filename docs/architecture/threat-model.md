# Platform-Wide Threat Model

This document establishes the platform-level threat model for the **LOTA Security Platform**, detailing assets, threat actors, trust boundaries, abuse cases, mitigations, and non-goals.

---

## 1. Protected Assets

1. **Customer Source Code & Artifacts**: Proprietary IP and binaries submitted for analysis.
2. **Security Findings & Evidence**: Vulnerability details, secret locations, and architectural weaknesses.
3. **Connector & Platform Credentials**: API tokens, private keys, database credentials, and cloud secrets.
4. **Audit Logs & State Ledger**: Tamper-evident records of scans, exceptions, and remediation actions.
5. **Policy Definitions**: OPA Rego bundles governing compliance and security posture.

---

## 2. Threat Actors & Motivations

| Actor Profile | Description | Motivation |
|---|---|---|
| **External Attacker** | Internet-based adversary targeting public API endpoints. | Service disruption, SSRF to internal clouds, tenant data theft. |
| **Malicious Repository Author** | Adversary submitting trojanized repositories or artifacts. | Remote code execution on analysis workers, container breakout, supply chain tampering. |
| **Compromised Connector** | Third-party service (e.g. MISP, GitHub) returning malicious payloads. | Exploiting parser bugs, manipulating findings, denial of service. |
| **Malicious Insider / Tenant** | Authenticated user attempting privilege escalation. | Bypassing remediation approvals, altering audit history, viewing other tenants' data. |

---

## 3. Abuse Cases & Mitigations

### 3.1 Malicious Repository Code Execution
- **Threat**: Repository contains malicious build scripts (e.g., `setup.py`, Makefile, npm `postinstall`, or Git hooks) that trigger upon clone or inspection.
- **Mitigation**:
  - Clone with `--no-checkout` or disable Git hooks (`core.hooksPath=/dev/null`).
  - Workers run as unprivileged users (`nobody` or non-root UID 10001).
  - No shell execution of repository scripts during static analysis (Levels L0, L1, L2).
  - Isolated microVM or container sandboxing with dropped capabilities.

### 3.2 Server-Side Request Forgery (SSRF)
- **Threat**: Attacker submits repository URLs pointing to cloud metadata services (`http://169.254.169.254`) or internal network services.
- **Mitigation**:
  - Strict URL validation rejecting private RFC 1918/RFC 3927 addresses and loopback addresses.
  - DNS resolution validation before fetch.
  - Workers operate with egress deny-by-default; network namespaces forbid unapproved outbound traffic.

### 3.3 Secret Leakage in Findings or Logs
- **Threat**: Secret scanners detect valid credentials and print them in logs, error traces, or unmasked findings.
- **Mitigation**:
  - Centralized redaction library (`lota_common.redaction`) active across all pipelines.
  - Masking secrets prior to database persistence and UI rendering.
  - Structured logging filters rejecting Authorization headers and sensitive keys.

### 3.4 Sandbox Escape & Host Compromise
- **Threat**: Malicious container or artifact exploits container runtime vulnerabilities to access host kernel or filesystem.
- **Mitigation**:
  - Never mount the Docker socket (`/var/run/docker.sock`).
  - Read-only root filesystem on worker containers.
  - Seccomp and AppArmor/SELinux profiles applied.
  - Disposable worker lifecycles (terminated after every task).

---

## 4. Platform Non-Goals

- The platform will **never** execute offensive exploits against external systems.
- The platform will **never** perform brute-force credential stuffing or password attacks.
- The platform will **not** automatically execute production-impacting remediations without explicit, signed human authorization.
