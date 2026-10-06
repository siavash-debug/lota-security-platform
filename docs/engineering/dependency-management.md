# Dependency Management Policy

Third-party dependencies represent supply chain risk. The **LOTA Security Platform** maintains rigorous dependency governance.

---

## 1. Principles

1. **Explicit Pinning**: All production dependencies and container base images must specify exact versions or cryptographic digests.
2. **Automated Auditing**: Dependabot and vulnerability scanners continuously audit dependencies for known CVEs.
3. **Minimal Attack Surface**: Minimize the number of external packages. Favor standard library modules where feasible.
4. **SBOM Generation**: All released components must publish a CycloneDX or SPDX Software Bill of Materials.

---

## 2. Python Dependencies

- Use `pyproject.toml` standards.
- Production images lock dependencies with exact version constraints.
- Avoid unverified packages or packages with suspicious maintainer histories.
