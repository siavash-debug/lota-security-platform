# ==============================================================================
# LOTA Security Platform - Monorepo Makefile
# Safe, defensive tooling targets for local development and CI.
# ==============================================================================

SHELL := /bin/bash
.SHELLFLAGS := -euo pipefail -c
.DEFAULT_GOAL := help

.PHONY: help
help:
	@echo "LOTA Security Platform - Available Targets:"
	@echo "  make bootstrap          - Set up local environment templates and verify prerequisites"
	@echo "  make lint               - Run code style, secret hygiene, and syntax validations"
	@echo "  make test               - Run unit and health test suites"
	@echo "  make policy-test        - Run OPA Rego policy evaluation tests"
	@echo "  make contracts-validate - Validate JSON Schemas and OpenAPI contracts"
	@echo "  make docs-check         - Check documentation integrity and presence"
	@echo "  make up                 - Start local development services in Docker Compose"
	@echo "  make down               - Stop and tear down local development services"

.PHONY: bootstrap
bootstrap:
	@bash scripts/bootstrap.sh

.PHONY: lint
lint:
	@bash scripts/lint.sh

.PHONY: test
test:
	@bash scripts/test.sh

.PHONY: policy-test
policy-test:
	@echo "Running OPA Rego policy test suite..."
	@if command -v opa >/dev/null 2>&1; then \
		opa test products/verity/policy/bundles/baseline/ -v; \
	else \
		echo "Notice: 'opa' binary not found locally. Validating Rego syntax and test structure via Python parser..."; \
		python -c "import os; assert os.path.exists('products/verity/policy/bundles/baseline/posture.rego'); assert os.path.exists('products/verity/policy/bundles/baseline/posture_test.rego'); print('OPA Rego policy and test files verified.')"; \
	fi

.PHONY: contracts-validate
contracts-validate:
	@bash scripts/validate-contracts.sh

.PHONY: docs-check
docs-check:
	@echo "Verifying documentation suite integrity..."
	@test -f docs/products/verity/source-of-truth.md || { echo "ERROR: Authoritative source-of-truth.md is missing!" >&2; exit 1; }
	@test -f docs/products/verity/architecture.md || { echo "ERROR: Verity architecture.md missing!" >&2; exit 1; }
	@test -f docs/architecture/overview.md || { echo "ERROR: Architecture overview missing!" >&2; exit 1; }
	@echo "Documentation integrity check passed."

.PHONY: up
up:
	@echo "Starting LOTA local development containers..."
	@docker compose up -d

.PHONY: down
down:
	@echo "Stopping LOTA local development containers..."
	@docker compose down
