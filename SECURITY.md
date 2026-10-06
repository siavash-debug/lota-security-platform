# Security Policy

LOTA Security is committed to ensuring the highest level of security across all software, infrastructure, and architectural designs within the platform.

---

## 1. Reporting a Vulnerability

If you discover a security vulnerability or potential threat in this codebase:

- **DO NOT** create a public issue, discussion thread, or pull request.
- Report the vulnerability via encrypted email to: `security@lota-security.internal` or via our coordinated disclosure program.
- Provide a detailed description including:
  - Affected components, services, or documentation.
  - Step-by-step reproduction instructions.
  - Potential impact assessment.
  - Any proposed defensive mitigations.

---

## 2. Response Timeline

The LOTA Security team adheres to the following response timeline:
- **Initial Acknowledgement**: Within 24 hours of receipt.
- **Triage and Impact Assessment**: Within 72 hours.
- **Mitigation/Patch Development**: Critical issues addressed within 7 days; high issues within 14 days.
- **Disclosure Coordination**: Coordinated public disclosure following verification of fixes.

---

## 3. Scope and Safe Harbor

This policy applies to all components of the `lota-security-platform` monorepo.

We support safe harbor protections for security researchers who:
- Conduct research in good faith without causing service disruption.
- Do not access, alter, or exfiltrate private customer data.
- Refrain from dynamic exploitation or denial-of-service tests against production systems.
- Give us reasonable time to remediate before public disclosure.

---

## 4. Platform Security Architecture

The platform operates on core defensive invariants:
- **Worker Isolation**: Scanners and analyzers run in unprivileged, network-isolated environments.
- **Zero Secrets in Logs**: Sensitive tokens and credentials are masked before storage or display.
- **Approval-Gated Remediation**: Remediation operations cannot run without recorded multi-party approvals.
- **Immutable Provenance**: Every scan and finding is anchored to an immutable digest.
