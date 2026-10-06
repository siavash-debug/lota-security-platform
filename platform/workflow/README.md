# Platform Workflow & Orchestration

This subsystem coordinates task queues, state machines, and worker scheduling across the **LOTA Security Platform**.

---

## 1. Capabilities

- **State Machine Engine**: Formal transition lifecycle tracking (`CREATED`, `QUEUED`, `RUNNING`, `SUCCEEDED`, `FAILED`).
- **Distributed Queuing**: Redis-backed asynchronous worker queues with strict job acknowledgement and timeout guards.
- **Idempotency Guarantees**: Deduping duplicate scan submissions using asset digest and policy hash keys.
- **Worker Auto-Scaling**: Dynamic scaling of worker container pools based on queue depth and tenant quotas.
