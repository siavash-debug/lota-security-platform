"""Secret redaction and sanitization utilities for LOTA Security Platform."""

from __future__ import annotations

import re
from typing import Any

# Sensitive dictionary keys to automatically mask
SENSITIVE_KEYS: set[str] = {
    "password",
    "passwd",
    "secret",
    "token",
    "access_token",
    "refresh_token",
    "api_key",
    "apikey",
    "private_key",
    "privkey",
    "certificate",
    "authorization",
    "auth",
    "cookie",
    "session",
    "session_id",
    "aws_secret_access_key",
    "jwt",
    "credentials",
}

# String regex patterns for common secrets
_REDACTION_PATTERNS: list[tuple[re.Pattern[str], str]] = [
    # Bearer tokens
    (re.compile(r"(?i)(Bearer\s+)[A-Za-z0-9\-_\.=]+"), r"\1[REDACTED]"),
    # AWS access keys
    (re.compile(r"\b(AKIA[0-9A-Z]{16})\b"), "[REDACTED_AWS_KEY]"),
    # GitHub tokens
    (re.compile(r"\b(ghp_[0-9a-zA-Z]{36})\b"), "[REDACTED_GITHUB_TOKEN]"),
    # Generic API key query parameters
    (re.compile(r"(?i)(api[_-]?key=)[^&\s]+"), r"\1[REDACTED]"),
    # PEM Private keys
    (
        re.compile(r"-----BEGIN[ A-Z0-9_-]*PRIVATE KEY-----.*?-----END[ A-Z0-9_-]*PRIVATE KEY-----", re.DOTALL),
        "[REDACTED_PRIVATE_KEY]",
    ),
]

REDACTED_PLACEHOLDER = "[REDACTED]"


def redact_string(text: str) -> str:
    """Mask known secret patterns inside arbitrary text strings.

    Args:
        text: Input string potentially containing secret tokens.

    Returns:
        Sanitized string with matching secret patterns replaced.
    """
    if not isinstance(text, str):
        return str(text)

    sanitized = text
    for pattern, replacement in _REDACTION_PATTERNS:
        sanitized = pattern.sub(replacement, sanitized)
    return sanitized


def redact_sensitive_data(data: Any, max_depth: int = 10) -> Any:
    """Recursively redact sensitive keys from nested dictionaries, lists, and primitives.

    Args:
        data: Arbitrary Python structure (dict, list, str, etc.)
        max_depth: Maximum recursion depth to prevent infinite recursion.

    Returns:
        Deep copy of the data with sensitive keys and patterns masked.
    """
    if max_depth <= 0:
        return REDACTED_PLACEHOLDER

    if isinstance(data, dict):
        sanitized_dict: dict[str, Any] = {}
        for key, value in data.items():
            str_key = str(key).lower()
            if any(sensitive in str_key for sensitive in SENSITIVE_KEYS):
                sanitized_dict[key] = REDACTED_PLACEHOLDER
            else:
                sanitized_dict[key] = redact_sensitive_data(value, max_depth - 1)
        return sanitized_dict

    if isinstance(data, list):
        return [redact_sensitive_data(item, max_depth - 1) for item in data]

    if isinstance(data, tuple):
        return tuple(redact_sensitive_data(item, max_depth - 1) for item in data)

    if isinstance(data, set):
        return {redact_sensitive_data(item, max_depth - 1) for item in data}

    if isinstance(data, str):
        return redact_string(data)

    return data
