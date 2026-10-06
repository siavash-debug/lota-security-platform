# Verity Deployment Infrastructure

This directory contains deployment manifests, container definitions, and infrastructure-as-code scaffolding for **LOTA Security Verity**.

---

## 1. Directory Structure

```text
infrastructure/
├── README.md           # This document
├── docker/             # Hardened, unprivileged Dockerfiles for API, Worker, and Console
├── compose/            # Verity-specific Docker Compose integration manifests
├── kubernetes/         # Production Kubernetes base kustomization resources
└── terraform/          # Cloud infrastructure scaffolding templates
```

---

## 2. Hardening Invariants

- All container images run as non-root users (`UID 10001`).
- Base images must be pinned by SHA-256 digest in production.
- Production images must be signed using Cosign and publish CycloneDX SBOMs.
