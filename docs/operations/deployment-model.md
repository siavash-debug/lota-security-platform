# Deployment Model

This document outlines the deployment topologies supported by the **LOTA Security Platform**.

---

## 1. Environments

1. **Local Development**:
   - Single-node Docker Compose stack.
   - Minimal services: API, worker, PostgreSQL, Redis, MinIO, OPA.
   - Strictly localhost-bound ports.
2. **Production Topology**:
   - Cloud Kubernetes clusters (EKS, GKE, or AKS) or hardened on-premises OpenShift.
   - Managed cloud databases (AWS RDS PostgreSQL, Cloud SQL) with automated backups and encryption.
   - Managed object stores (AWS S3, Google Cloud Storage) with versioning, immutability, and server-side encryption.
   - Workload Identity / IAM Roles for service accounts; zero static credentials.
