---
name: Security Control Request
about: Propose a new security control, posture check, or compliance requirement
title: '[CONTROL] '
labels: ['security-control', 'compliance']
assignees: ''
---

## Control Specification
- Control Name:
- Proposed Control ID: (e.g. `CONTAINER-CAP-002`)
- Severity Classification: (Critical / High / Medium / Low / Info)

## Target Assessment Domain
- [ ] Git Repository & Provenance
- [ ] Dependency & SBOM
- [ ] Secret Exposure
- [ ] Container Image / Dockerfile
- [ ] Infrastructure-as-Code (Terraform / Kubernetes)
- [ ] CI/CD Pipeline Configuration
- [ ] Defensive Tool Posture (MISP / Suricata / Zeek)

## Rationale & Threat Model
Explain what risk this control identifies and what attack vector it mitigates.

## Evidence Requirements
What concrete, immutable evidence (AST node, line range, config value) must be captured to substantiate this finding?
