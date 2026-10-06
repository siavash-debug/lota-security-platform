# Multi-Tenancy Architecture Model

The **LOTA Security Platform** is engineered to support strict multi-tenant isolation, ensuring that organization assets, scan outputs, and findings are completely segmented.

---

## 1. Tenancy Model Overview

1. **Logical Data Partitioning**:
   - Every database table incorporates a mandatory `tenant_id` foreign key.
   - Row-Level Security (RLS) policies within PostgreSQL enforce tenant boundaries at the database engine level.
2. **Object Storage Segmentation**:
   - MinIO / S3 buckets isolate tenant evidence into dedicated prefix namespaces or separate encrypted buckets (`evidence/<tenant_id>/<scan_id>/`).
3. **Execution Compute Isolation**:
   - Scan jobs execute within ephemeral worker containers provisioned exclusively for a single tenant job.
   - Workers are torn down and their local disk volumes securely wiped upon task completion.
4. **Encryption Key Separation**:
   - Envelope encryption utilizes tenant-specific Key Encryption Keys (KEKs) managed within HashiCorp Vault or cloud KMS.
