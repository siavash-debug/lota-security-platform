"""Audit event data models and utilities for LOTA Security Platform."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any
from pydantic import BaseModel, Field

from lota_common.ids import generate_id
from lota_common.redaction import redact_sensitive_data


class AuditActor(BaseModel):
    """Represents the identity triggering an audit event."""

    user_id: str = Field(description="Unique identifier of the actor")
    role: str = Field(default="user", description="Assigned role of the actor")
    tenant_id: str | None = Field(default=None, description="Optional tenant identifier")


class AuditTarget(BaseModel):
    """Represents the subject resource modified or accessed."""

    entity_type: str = Field(description="Domain entity type (asset, scan, finding, etc.)")
    entity_id: str = Field(description="Identifier of the target entity")


class AuditEvent(BaseModel):
    """Immutable audit record conforming to audit-event.schema.json."""

    event_id: str = Field(
        default_factory=lambda: generate_id("event"),
        description="Unique prefixed event identifier",
    )
    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="ISO 8601 UTC timestamp of the event",
    )
    actor: AuditActor = Field(description="The authenticated actor performing the action")
    action: str = Field(description="Canonical action string (e.g. 'asset.create', 'scan.start')")
    target: AuditTarget = Field(description="The primary target resource of the action")
    status: str = Field(default="SUCCESS", description="Outcome: SUCCESS, FAILURE, or DENIED")
    metadata: dict[str, Any] = Field(
        default_factory=dict,
        description="Sanitized contextual metadata (IP, user agent, request ID)",
    )


def create_audit_event(
    action: str,
    actor: dict[str, Any] | AuditActor,
    target: dict[str, Any] | AuditTarget,
    status: str = "SUCCESS",
    metadata: dict[str, Any] | None = None,
) -> AuditEvent:
    """Safely construct a sanitized audit event record.

    Args:
        action: Canonical action string.
        actor: Actor dictionary or AuditActor instance.
        target: Target dictionary or AuditTarget instance.
        status: Operation outcome status.
        metadata: Optional contextual metadata (will be redacted automatically).

    Returns:
        A validated, immutable AuditEvent instance.
    """
    if isinstance(actor, dict):
        # Support either actor={'user_id': ...} or flat actor dict
        u_id = actor.get("user_id") or actor.get("id") or "anonymous"
        r = actor.get("role", "unknown")
        t = actor.get("tenant_id")
        actor_obj = AuditActor(user_id=u_id, role=r, tenant_id=t)
    else:
        actor_obj = actor

    if isinstance(target, dict):
        e_type = target.get("entity_type") or next(
            (k.replace("_id", "") for k in target if k.endswith("_id")), "unknown"
        )
        e_id = target.get("entity_id") or target.get(f"{e_type}_id") or "unknown"
        target_obj = AuditTarget(entity_type=e_type, entity_id=str(e_id))
    else:
        target_obj = target

    safe_metadata = redact_sensitive_data(metadata or {})

    return AuditEvent(
        action=action,
        actor=actor_obj,
        target=target_obj,
        status=status,
        metadata=safe_metadata,
    )
