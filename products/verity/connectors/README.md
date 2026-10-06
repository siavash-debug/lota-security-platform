# Verity Read-Only Security Connectors

This directory contains adapter specifications for integrating **LOTA Security Verity** with source management platforms, container registries, and defensive security tool deployments.

---

## 1. Connector Invariants

1. **Strictly Read-Only**: Connectors query APIs or parse exported configurations. They **never** modify settings on external systems.
2. **Credential Minimization**: Connectors utilize scoped, short-lived tokens restricted to the exact endpoints required.
3. **No Arbitrary Execution**: External API responses are validated against schemas before passing to the normalization engine.

---

## 2. Connector Index

- **[`base/`](file:///products/verity/connectors/base/README.md)**: Common connector interface and error contracts.
- **[`github/`](file:///products/verity/connectors/github/README.md)**: GitHub repository and workflow posture connector.
- **[`container-registry/`](file:///products/verity/connectors/container-registry/README.md)**: OCI registry metadata and layer connector.
- **[`misp/`](file:///products/verity/connectors/misp/README.md)**: MISP read-only configuration posture connector.
- **[`suricata/`](file:///products/verity/connectors/suricata/README.md)**: Suricata NIDS configuration and sensor posture connector.
- **[`zeek/`](file:///products/verity/connectors/zeek/README.md)**: Zeek network monitor posture connector.
