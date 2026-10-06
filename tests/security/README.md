# Security & Defensive Regression Tests

This test suite verifies critical defensive invariants of the platform:
- Verifies that Authorization headers and secret tokens never leak into structured logs.
- Asserts that worker containers drop capabilities and run as unprivileged non-root users.
- Validates that SSRF protections block private IP ranges and loopback metadata services.
