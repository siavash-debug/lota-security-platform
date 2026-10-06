# GitHub Posture Connector

Evaluates the security posture of GitHub organizations and repositories in read-only mode.

---

## 1. Scope of Posture Checks

- Commit signing enforcement and signed tag verification.
- Branch protection rules (required reviews, dismissal restrictions).
- Presence of `SECURITY.md`, `CODEOWNERS`, and license files.
- GitHub Actions workflow posture (unpinned SHA actions, `pull_request_target` usage).
- Secret scanning alerts and Dependabot status via read-only APIs.
