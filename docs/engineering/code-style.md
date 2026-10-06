# Code Style & Quality Standards

This document establishes style guidelines across languages in the **LOTA Security Platform**.

---

## 1. General Standards

- **Language**: All code identifiers, docstrings, comments, log messages, commit messages, and documentation must be written in **English only**.
- **Formatting**: Adhere to `.editorconfig` (UTF-8, LF line endings, 2 spaces for YAML/JSON/Markdown, 4 spaces for Python).

---

## 2. Python Standards

- Target Python: **3.12+**.
- Type Annotations: Full static type annotations on all functions, classes, and public interfaces.
- Pydantic: Use Pydantic v2 for configuration settings, data validation, and contract models.
- Logging: Use structured JSON logging; never format string interpolations containing raw request bodies or auth tokens.
- Exceptions: Inherit from custom exceptions defined in `lota_common.errors`.

---

## 3. Policy (Rego) Standards

- Rules must evaluate cleanly without runtime side effects.
- Rule decisions should emit structured messages, confidence levels, and severity classifications.
- Each policy bundle must include a companion `*_test.rego` file covering compliant and non-compliant states.
