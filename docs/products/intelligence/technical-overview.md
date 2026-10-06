# LOTA Security Intelligence - Technical Overview

> **Document Status**: Conceptual Architecture (Not implemented in this repository)

---

## 1. Architectural Intent

LOTA Security Intelligence is envisioned to deliver automated threat intelligence aggregation, normalization, and contextualization for enterprise defense teams.

---

## 2. Intended Capabilities

- **Indicator Ingestion & Normalization**: Ingest indicators of compromise (IOCs) from commercial feeds, open-source CTI (e.g., MISP, AlienVault OTX), and internal incidents into STIX 2.1 format.
- **TTP Mapping**: Correlate adversary behaviors against the MITRE ATT&CK enterprise matrix.
- **Enrichment Pipelines**: Query DNS, WHOIS, ASN, reputation databases, and sandbox detonations in read-only workflows.
- **Intelligence Sharing**: Support TAXII 2.1 collection endpoints and selective sharing circles with automated TLP sanitization.

---

## 3. Implementation Status

This product currently has **no active code implementation** in this monorepo commit. All implementation will occur in later roadmap phases following Verity maturation.
