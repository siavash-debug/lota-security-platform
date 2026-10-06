"""LOTA Common Package.

Shared defensive primitives, ID generation, secret redaction, error taxonomy,
and audit models across the LOTA Security Platform suite.
"""

from lota_common.audit import AuditEvent, create_audit_event
from lota_common.errors import (
    AuthenticationError,
    AuthorizationError,
    ConflictError,
    NotFoundError,
    PlatformError,
    RedactionError,
    ValidationError,
)
from lota_common.ids import generate_correlation_id, generate_id, generate_request_id, validate_id
from lota_common.redaction import redact_sensitive_data, redact_string

__all__ = [
    "generate_id",
    "generate_request_id",
    "generate_correlation_id",
    "validate_id",
    "redact_sensitive_data",
    "redact_string",
    "AuditEvent",
    "create_audit_event",
    "PlatformError",
    "ValidationError",
    "NotFoundError",
    "ConflictError",
    "AuthenticationError",
    "AuthorizationError",
    "RedactionError",
]
