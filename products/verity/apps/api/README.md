# LOTA Security Verity - API Gateway Scaffold

This directory houses the FastAPI control plane gateway for **LOTA Security Verity**.

---

## 1. Responsibilities

- Exposes health, readiness, and version diagnostic endpoints.
- Validates request payload schemas using Pydantic models.
- Injects `X-Request-ID` and correlation context via ASGI middleware.
- Implements structured JSON logging with automated redaction of sensitive credentials and headers.
- Safe placeholder scaffolding: State-changing posture scanning and remediation endpoints return `501 Not Implemented`.

---

## 2. Invariants

- **Zero Blind Execution**: No endpoint clones repositories, downloads external files, or runs shell commands.
- **Header Sanitization**: Authorization headers and credentials are never emitted into logs.
