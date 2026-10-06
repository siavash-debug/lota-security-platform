# Suricata Posture Connector

Evaluates the configuration posture, sensor health, and rule freshness of Suricata Network Threat Detection engines in read-only mode.

---

## 1. Scope of Posture Checks

- Engine version lifecycle and CVE exposure.
- Rule source integrity, signature freshness, and update timestamps.
- Configuration drift against baseline hardened yaml templates.
- Sensor drop rate, packet capture interface errors, and logging delivery.
