# Backup and Restore Procedures

This runbook documents backup and recovery mechanisms for data stores in the **LOTA Security Platform**.

---

## 1. Protected Data Stores

1. **PostgreSQL**: Stores assets, scan metadata, findings, policy exceptions, and the immutable audit ledger.
2. **MinIO / Object Storage**: Stores encrypted evidence files, AST snapshots, and SBOM artifacts.

---

## 2. Backup Schedules

- **PostgreSQL**: Continuous Write-Ahead Log (WAL) archiving combined with daily full database snapshots retained for 30 days.
- **Object Storage**: S3 object versioning enabled with cross-region replication and immutable WORM retention where required by compliance.

---

## 3. Restoration Runbook

1. Provision an isolated recovery database instance.
2. Restore point-in-time snapshot using WAL archives.
3. Verify integrity of audit ledger table signatures and row hashes.
4. Validate schema migrations before switching application traffic.
