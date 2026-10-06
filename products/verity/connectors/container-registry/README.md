# Container Registry Connector

Interrogates OCI-compliant container registries in read-only mode to retrieve image manifests, layer digests, and signatures.

---

## 1. Scope of Posture Checks

- Resolution of mutable image tags to immutable cryptographic digests.
- Multi-architecture manifest inspection.
- Sigstore Cosign or Notary signature presence.
- Layer count, uncompressed size, and base image provenance.
