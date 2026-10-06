# Policy Authoring Guide

This guide details best practices for authoring declarative security posture rules using Open Policy Agent (OPA) and Rego.

---

## 1. Rule Architecture

Each policy evaluates a normalized input document (`input`) conforming to `scan-input.schema.json`.

Policies emit decisions under structured sets:
- `deny[msg]`: Emitted when a hard security violation occurs.
- `warn[msg]`: Emitted when a suboptimal posture is detected that does not violate a mandatory control.

```rego
package posture

# Ensure administrative endpoints are never exposed to public internet
deny[msg] {
    input.asset.type == "misp"
    input.controls.public_admin_exposure == true
    msg := "MISP administrative interface is publicly reachable."
}
```

---

## 2. Testing Mandates

Every policy rule must be accompanied by unit tests in a corresponding `*_test.rego` file. Tests must assert:
1. `deny` or `warn` triggers on non-compliant fixtures.
2. Zero violations trigger on fully compliant fixtures.
