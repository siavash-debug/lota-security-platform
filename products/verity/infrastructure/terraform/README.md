# Verity Cloud Infrastructure (Terraform)

This directory contains Terraform Infrastructure-as-Code modules for provisioning backing cloud services for **LOTA Security Verity**.

---

## 1. Managed Cloud Resources (Production Target)

- Managed PostgreSQL (AWS RDS / GCP Cloud SQL) with encryption and automated WAL archiving.
- Managed Object Storage (AWS S3 / GCS) with KMS server-side encryption and versioning.
- Managed Secret Storage (HashiCorp Vault / AWS Secrets Manager).
- Managed OIDC Identity Integrations.
