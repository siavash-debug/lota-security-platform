# Verity Kubernetes Deployment Scaffolding

This directory contains declarative Kubernetes manifests and Kustomize bases for deploying **LOTA Security Verity** into hardened cluster environments.

---

## 1. Directory Structure

```text
kubernetes/
├── README.md
└── base/
    └── kustomization.yaml
```

---

## 2. Hardening Requirements

- Run all containers with `securityContext.runAsNonRoot: true`, `readOnlyRootFilesystem: true`, and `allowPrivilegeEscalation: false`.
- NetworkPolicies must enforce egress deny-by-default for worker pods.
