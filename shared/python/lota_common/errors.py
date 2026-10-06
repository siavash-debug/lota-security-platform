"""Structured error taxonomies and exceptions for LOTA Security Platform."""

from __future__ import annotations

from typing import Any


class PlatformError(Exception):
    """Base exception for all domain and system errors within LOTA Security."""

    def __init__(
        self,
        message: str,
        error_code: str = "PLATFORM_ERROR",
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.error_code = error_code
        self.details = details or {}

    def to_dict(self) -> dict[str, Any]:
        """Convert the exception into a structured API error dictionary."""
        return {
            "error_code": self.error_code,
            "message": self.message,
            "details": self.details,
        }


class ValidationError(PlatformError):
    """Raised when request payload or schema validation fails."""

    def __init__(self, message: str, details: dict[str, Any] | None = None) -> None:
        super().__init__(message, error_code="VALIDATION_ERROR", details=details)


class AuthenticationError(PlatformError):
    """Raised when authentication credentials are missing, invalid, or expired."""

    def __init__(self, message: str = "Authentication failed", details: dict[str, Any] | None = None) -> None:
        super().__init__(message, error_code="AUTHENTICATION_FAILED", details=details)


class AuthorizationError(PlatformError):
    """Raised when authenticated caller lacks required permissions."""

    def __init__(self, message: str = "Access denied", details: dict[str, Any] | None = None) -> None:
        super().__init__(message, error_code="AUTHORIZATION_DENIED", details=details)


class NotFoundError(PlatformError):
    """Raised when a requested resource is not found."""

    def __init__(self, message: str, details: dict[str, Any] | None = None) -> None:
        super().__init__(message, error_code="NOT_FOUND", details=details)


class ConflictError(PlatformError):
    """Raised when an operation conflicts with current resource state."""

    def __init__(self, message: str, details: dict[str, Any] | None = None) -> None:
        super().__init__(message, error_code="CONFLICT", details=details)


class RedactionError(PlatformError):
    """Raised when a secret redaction filter encounters an irrecoverable error."""

    def __init__(self, message: str, details: dict[str, Any] | None = None) -> None:
        super().__init__(message, error_code="REDACTION_ERROR", details=details)
