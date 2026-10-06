# Developer Tooling & Scanner Wrappers

This directory contains developer utility scripts and specifications for scanner wrappers used in the **LOTA Security Platform**.

---

## 1. Directory Structure

```text
tools/
├── README.md               # This document
├── scripts/                # Developer and DevSecOps maintenance scripts
└── scanner-wrappers/       # Containerized wrappers for third-party security scanners
    ├── trivy/              # Container vulnerability and misconfiguration scanner
    ├── gitleaks/           # Secret and credential scanner
    ├── semgrep/            # Static code analysis (SAST) engine
    ├── syft/               # SBOM generator
    └── grype/              # SBOM vulnerability matcher
```
