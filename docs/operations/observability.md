# Observability & Monitoring

The **LOTA Security Platform** incorporates three pillars of observability: structured logging, metrics, and distributed tracing.

---

## 1. Structured JSON Logging

- Every log line is formatted as a single JSON object.
- Required standard fields:
  - `timestamp`: ISO 8601 UTC timestamp.
  - `level`: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`.
  - `service`: Service identifier (e.g. `verity-api`, `verity-worker`).
  - `request_id`: Correlation ID passed across HTTP requests.
  - `message`: Descriptive message string in English.
- Sensitive values (tokens, credentials, Authorization headers) are automatically stripped before emission.

---

## 2. Distributed Tracing & Metrics

- OpenTelemetry instrumentation for distributed tracing across API gateway, queue handlers, and worker jobs.
- Prometheus-compatible metrics endpoint exposed internally on `/metrics`.
