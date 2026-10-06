# Baseline Security Posture Bundle

This package implements the foundational Open Policy Agent (OPA) Rego rules evaluating normalized security findings against organizational posture standards.

---

## 1. Rule Catalog

- **`POSTURE-MISP-001`**: Detects public administrative exposure on sensitive tools (MISP).
- **`POSTURE-MFA-001`**: Detects missing MFA on privileged administrative tools (Velociraptor).
- **`POSTURE-KEY-001`**: Warns when API keys exceed standard maximum age threshold (>90 days).
- **`POSTURE-CONT-001`**: Denies containers executing as root (`USER root`).
- **`POSTURE-SOCK-001`**: Denies mounting the host Docker socket into containers.

---

## 2. Execution

These rules are static declarations tested against offline fixtures. They do **not** directly execute changes against production systems.
