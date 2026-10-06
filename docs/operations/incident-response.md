# Incident Response Plan

This document establishes the incident response plan for operational and security incidents affecting the **LOTA Security Platform**.

---

## 1. Incident Severity Levels

| Level | Definition | Response SLA |
|---|---|---|
| **SEV-1 (Critical)** | Data breach, control plane compromise, worker sandbox breakout, widespread data loss. | Immediate (15 minutes). |
| **SEV-2 (High)** | Degradation of scanning pipeline, authentication failure, unauthorized exception creation. | Within 1 hour. |
| **SEV-3 (Medium)** | Connector failure, degraded worker performance, non-critical telemetry gap. | Within 4 hours. |
| **SEV-4 (Low)** | Minor bug, cosmetic UI issue, documentation error. | Next business day. |

---

## 2. Response Phases

1. **Identification**: Triage alert through SIEM/PagerDuty; assign incident commander.
2. **Containment**: Isolate affected worker pods, revoke compromised connector tokens, block malicious repository domains at the API gateway.
3. **Eradication**: Terminate rogue workers, roll back policy changes, patch vulnerabilities.
4. **Recovery**: Restore verified state from backups, test pipeline integrity, resume operations.
5. **Post-Mortem**: Document root cause, timeline, lessons learned, and defensive action items.
