"""Application configuration settings for LOTA Security Verity API."""

from __future__ import annotations

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Verity API environment configuration settings."""

    service_name: str = "verity-api"
    app_name: str = "LOTA Security Verity"
    version: str = "0.1.0"
    environment: str = "development"
    build: str = "development-scaffold"
    revision: str = "initial-commit"

    log_level: str = "INFO"
    api_host: str = "127.0.0.1"
    api_port: int = 8000

    postgres_host: str = "127.0.0.1"
    postgres_port: int = 5432
    postgres_db: str = "lota_verity_dev"
    postgres_user: str = "verity_dev_user"
    postgres_password: str = "dev_only_verity_password_insecure"

    redis_host: str = "127.0.0.1"
    redis_port: int = 6379

    minio_endpoint: str = "127.0.0.1:9000"
    opa_url: str = "http://127.0.0.1:8181/v1/data/posture"

    model_config = SettingsConfigDict(
        env_prefix="VERITY_",
        env_file=".env",
        extra="ignore",
    )


settings = Settings()
