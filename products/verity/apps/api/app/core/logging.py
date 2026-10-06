"""Structured JSON logging configuration for LOTA Security Verity API."""

from __future__ import annotations

import json
import logging
import sys
from datetime import datetime, timezone
from typing import Any

from lota_common.redaction import redact_sensitive_data


class StructuredJsonFormatter(logging.Formatter):
    """Custom formatter emitting structured, redacted JSON log lines."""

    def format(self, record: logging.LogRecord) -> str:
        log_payload: dict[str, Any] = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }

        # Include custom extra fields (e.g. request_id, service, actor)
        if hasattr(record, "request_id"):
            log_payload["request_id"] = record.request_id
        if hasattr(record, "service"):
            log_payload["service"] = record.service
        if hasattr(record, "details") and isinstance(record.details, dict):
            log_payload["details"] = record.details

        if record.exc_info and record.exc_text:
            log_payload["exception"] = record.exc_text

        # Sanitize sensitive fields before converting to string
        safe_payload = redact_sensitive_data(log_payload)
        return json.dumps(safe_payload)


def setup_logging(level_name: str = "INFO", service_name: str = "verity-api") -> logging.Logger:
    """Initialize structured JSON logging for the application."""
    root_logger = logging.getLogger()
    root_logger.setLevel(level_name.upper())

    # Clear existing handlers
    root_logger.handlers.clear()

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(StructuredJsonFormatter())
    root_logger.addHandler(handler)

    logger = logging.getLogger(service_name)
    return logger
