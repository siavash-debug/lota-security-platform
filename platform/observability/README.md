# Platform Observability

This subsystem provides centralized telemetry, tracing, metrics, and log pipelines for the **LOTA Security Platform**.

---

## 1. Capabilities

- **Structured JSON Logging**: Standard log emission across all microservices and workers.
- **Distributed Tracing**: OpenTelemetry trace context propagation across API gateways, queues, and scan workers.
- **Metrics Collection**: Prometheus counters, gauges, and histograms for scan throughput, worker latency, and queue depths.
- **Redaction Gate**: In-flight sanitization preventing sensitive tokens and credentials from reaching logging sinks.
