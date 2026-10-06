# Contributing to LOTA Security Platform

Thank you for your interest in contributing to the **LOTA Security Platform**. We maintain strict DevSecOps, engineering, and security hygiene standards across our monorepo.

---

## 1. Code of Conduct

All contributors and maintainers are expected to abide by our [Code of Conduct](file:///CODE_OF_CONDUCT.md). Please report unacceptable behavior to `security@lota-security.internal`.

---

## 2. DevSecOps & Architectural Tenets

When contributing to this repository, keep our foundational principles in mind:
- **Defense in Depth**: Zero trust networking, least privilege access, and strict input validation.
- **Evidence-First**: Every assessment finding must reference concrete, immutable evidence.
- **No Blind Execution**: Never introduce code paths that execute untrusted code or repository contents on the control plane or developer workstations.
- **English Only**: All documentation, code comments, pull requests, issue descriptions, and commit messages must be in English.
- **Immutability**: Ensure scans and findings pin exact commit SHAs or image digests.

---

## 3. Getting Started

### Local Setup
1. Fork or clone the repository.
2. Review prerequisites in [Local Development Guide](file:///docs/engineering/local-development.md).
3. Create local configuration:
   ```bash
   cp .env.example .env
   cp compose/dev.env.example compose/dev.env
   ```
4. Run bootstrap checks:
   ```bash
   make bootstrap
   ```

### Branching & Commit Conventions
- Branch naming: `feat/<feature-name>`, `fix/<bug-name>`, `docs/<topic>`, `chore/<task>`.
- Commit messages should follow Conventional Commits (e.g., `feat(verity-api): add asset validation model`).

---

## 4. Development Workflow & Verification

Before submitting a Pull Request, run the required local validation suite:
```bash
make lint
make test
make policy-test
make contracts-validate
```

All CI checks must pass cleanly. Pull requests that introduce unpinned actions, hardcoded credentials, or insecure defaults will be rejected.

---

## 5. Security Vulnerability Disclosures

**Do not file public GitHub issues for security vulnerabilities.**  
Please follow the disclosure procedure defined in [SECURITY.md](file:///SECURITY.md).
