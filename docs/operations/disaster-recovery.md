# Disaster Recovery Plan

This document describes the disaster recovery architecture and recovery procedures for the **LOTA Security Platform**.

---

## 1. Objectives

- **Recovery Point Objective (RPO)**: <= 1 hour (data loss window).
- **Recovery Time Objective (RTO)**: <= 4 hours (service restoration time).

---

## 2. Recovery Strategy

1. **Multi-Region Redundancy**:
   - Primary control plane deployed in region A; cold standby infrastructure manifests maintained in region B via GitOps.
2. **Data Replication**:
   - Cross-region asynchronous replication for PostgreSQL databases.
   - S3 cross-region bucket replication for evidence and artifact stores.
3. **Failover Execution**:
   - Promote replica database to primary.
   - Deploy Kubernetes manifests to secondary region cluster via ArgoCD/Flux.
   - Update DNS routing to point to secondary region ingress gateway.
