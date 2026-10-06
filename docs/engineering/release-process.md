# Release Process

This document defines the release engineering pipeline for the **LOTA Security Platform**.

---

## 1. Release Lifecycle

```text
[Main Branch] ──> [Pre-release Validation] ──> [Signed Release Tag] ──> [Immutable Artifacts + SBOM]
```

1. **Pre-release Checks**:
   - All CI pipelines pass (formatting, linting, unit tests, contract checks, CodeQL, policy tests).
   - Zero critical or high unresolved vulnerabilities in dependencies.
2. **Tagging & Signing**:
   - Releases use Semantic Versioning (`vMAJOR.MINOR.PATCH`).
   - Git tags are cryptographically signed with GPG or Sigstore Cosign.
3. **Artifact Provenance**:
   - Container images and release packages generate SLSA provenance attestations and CycloneDX SBOMs.
   - Container images are pushed to enterprise registries with immutable digests.
