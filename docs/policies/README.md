# Policy-as-Code Framework

The **LOTA Security Platform** utilizes Policy-as-Code (Open Policy Agent with Rego) to evaluate normalized security facts and determine organizational compliance.

---

## 1. Documentation Index

- **[Policy Authoring Guide](file:///docs/policies/policy-authoring-guide.md)**: How to write, structure, and test OPA Rego policy bundles.
- **[Exception Management](file:///docs/policies/exception-management.md)**: Lifecycle, justification, and approval gates for expiring policy exceptions.
- **[Remediation Approval](file:///docs/policies/remediation-approval.md)**: Multi-party authorization workflows for remediation proposals.

---

## 2. Directory Mappings

- Production policy bundles: `products/verity/policy/bundles/`
- Policy JSON input schemas: `products/verity/policy/schemas/`
- Test fixtures (compliant & non-compliant): `products/verity/policy/fixtures/`
