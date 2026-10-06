# LOTA Security Verity - Platform Limitations & Non-Goals

> **Authoritative Specification Reference**: Section 1 ("Product Definition") and Section 19 ("Explicit Non-Goals") of [`source-of-truth.md`](file:///docs/products/verity/source-of-truth.md).

---

## 1. Safety & Certification Reality

**LOTA Security Verity does NOT certify that any software, container image, or repository is secure or free of vulnerabilities.**

The platform produces a repeatable, evidence-backed assessment of known risks, observed code capabilities, and detected configuration weaknesses. It cannot prove the absence of zero-day vulnerabilities, malicious backdoors, or complex logic flaws.

---

## 2. Technical Limitations

1. **Static Analysis Limitations (False Positives & False Negatives)**:
   - Static analysis tools rely on AST pattern matching and heuristic rules. They inherently produce false positives (flagging benign patterns) and false negatives (missing obfuscated or runtime-constructed attacks).
2. **Dynamic Analysis Coverage**:
   - Sandboxed dynamic analysis (L4) observes only executed execution paths. Logic hidden behind specific environment flags, time-bombs, or evasive anti-analysis techniques may remain undetected.
3. **Repository Analysis Coverage**:
   - Repository posture checks cannot guarantee that deployed production artifacts match source code unless cryptographic build provenance (SLSA) and reproducible builds are enforced.

---

## 3. Organizational Non-Goals

- Verity is **not** a replacement for a professional manual code audit.
- Verity is **not** a replacement for an authorized third-party penetration test.
- Verity is **not** an automated exploit generator or offensive scanning tool.
- Verity will **not** automatically apply production remediations without human review.
