"""FastAPI application entry point for LOTA Security Verity API Gateway."""

from __future__ import annotations

import time
from typing import Callable
from fastapi import FastAPI, Request, Response, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.api.health import router as health_router
from app.core.config import settings
from app.core.logging import setup_logging
from app.core.security import extract_request_id

# Initialize structured logging
logger = setup_logging(level_name=settings.log_level, service_name=settings.service_name)

app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    description="Control plane API gateway for evidence-driven security posture assessment.",
    docs_url="/docs",
    redoc_url="/redoc",
)


@app.middleware("http")
async def request_context_middleware(request: Request, call_next: Callable) -> Response:
    """Security & Context Middleware:

    - Assigns and propagates X-Request-ID.
    - Measures request duration.
    - Emits structured JSON access logs without logging request bodies or sensitive headers.
    """
    request_id = extract_request_id(request)
    request.state.request_id = request_id

    start_time = time.perf_counter()

    # Log incoming request metadata (method and path only; NEVER headers or bodies)
    logger.info(
        f"Incoming HTTP {request.method} {request.url.path}",
        extra={"request_id": request_id, "service": settings.service_name},
    )

    try:
        response = await call_next(request)
    except Exception as exc:
        duration_ms = (time.perf_counter() - start_time) * 1000.0
        logger.error(
            f"Unhandled exception during HTTP {request.method} {request.url.path}: {str(exc)}",
            exc_info=True,
            extra={"request_id": request_id, "service": settings.service_name},
        )
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "error_code": "INTERNAL_SERVER_ERROR",
                "message": "An unexpected error occurred. Please contact security operations.",
                "request_id": request_id,
            },
            headers={"X-Request-ID": request_id},
        )

    duration_ms = (time.perf_counter() - start_time) * 1000.0
    response.headers["X-Request-ID"] = request_id

    logger.info(
        f"Completed HTTP {request.method} {request.url.path} with status {response.status_code} in {duration_ms:.2f}ms",
        extra={"request_id": request_id, "service": settings.service_name},
    )

    return response


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
    """Handle request validation errors safely without echoing sensitive payload details."""
    request_id = getattr(request.state, "request_id", "unknown")
    logger.warning(
        f"Request validation failure on {request.url.path}",
        extra={"request_id": request_id, "service": settings.service_name},
    )
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "error_code": "VALIDATION_ERROR",
            "message": "Input validation failed. Please check your request parameters.",
            "request_id": request_id,
            "details": exc.errors(),
        },
        headers={"X-Request-ID": request_id},
    )


# Mount routes
app.include_router(health_router)
