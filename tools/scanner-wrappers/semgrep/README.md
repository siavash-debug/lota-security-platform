# Semgrep SAST Integration

Wrapper specification for Semgrep static code analysis.

---

## 1. Scope

- Performs AST-based semantic code analysis across multiple languages.
- Detects dangerous capabilities (e.g. `eval`, `subprocess(shell=True)`, unsafe deserialization).
- Enforces community and custom security rule sets without executing repository code.
