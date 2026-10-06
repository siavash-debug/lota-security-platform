# Security Scanner Wrappers

This directory contains specifications and execution policies for open-source security tools integrated into the Verity worker pipeline.

---

## 1. Safety Policies

- Scanners execute inside unprivileged worker containers with dropped capabilities.
- Scanners run against static filesystem snapshots only (no network queries during scanning).
- Raw scanner JSON output is sanitized and passed to the normalization layer before persistence.
