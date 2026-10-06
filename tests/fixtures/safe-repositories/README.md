# Safe Repository Test Fixtures

This directory houses curated benchmark repository fixtures designed to pass all baseline posture and static analysis checks with zero findings.

---

## 1. Fixture Requirements

- All dependencies pinned to fixed, non-vulnerable versions.
- Pinned commit SHAs and signed tags.
- Compliant Dockerfiles executing as non-root users (`USER 10001`).
- Zero embedded secrets or sensitive patterns.
- Valid `LICENSE`, `SECURITY.md`, and `README.md` files.
