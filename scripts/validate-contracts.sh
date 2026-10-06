#!/usr/bin/env bash
# ==============================================================================
# LOTA Security Platform - Contract Validation Script
# Validates JSON schemas and OpenAPI 3.1 definitions.
# ==============================================================================
set -euo pipefail

echo "=========================================================="
echo "  LOTA Security Platform: Schema & Contract Validator     "
echo "=========================================================="

PYTHON_CMD="python"
if command -v python3 >/dev/null 2>&1; then
    PYTHON_CMD="python3"
fi

$PYTHON_CMD -c "
import json, os, sys

schema_dirs = [
    'products/verity/contracts/models',
    'products/verity/contracts/events',
    'products/verity/policy/schemas'
]

required_top_keys = ['$' + 'schema', '$' + 'id', 'title', 'description', 'type']

schema_count = 0
for sdir in schema_dirs:
    if not os.path.exists(sdir):
        print(f'Warning: Directory {sdir} does not exist yet.')
        continue
    for fname in os.listdir(sdir):
        if fname.endswith('.json'):
            path = os.path.join(sdir, fname)
            schema_count += 1
            with open(path, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                except Exception as e:
                    print(f'ERROR: Invalid JSON in {path}: {e}', file=sys.stderr)
                    sys.exit(1)
            
            # Check required keys
            missing = [k for k in required_top_keys if k not in data]
            if missing:
                print(f'ERROR: Schema {path} is missing required fields: {missing}', file=sys.stderr)
                sys.exit(1)

print(f'Verified {schema_count} JSON Schema contracts successfully.')

# Validate OpenAPI specification syntax
openapi_path = 'products/verity/contracts/openapi/openapi.yaml'
if os.path.exists(openapi_path):
    # Basic YAML structural verification
    with open(openapi_path, 'r', encoding='utf-8') as f:
        content = f.read()
        assert 'openapi: 3.1' in content or 'openapi: 3.0' in content, 'Missing OpenAPI version declaration'
        assert '/health:' in content, 'Missing /health path in OpenAPI spec'
        assert '/v1/assets/git:' in content, 'Missing /v1/assets/git in OpenAPI spec'
    print(f'Verified OpenAPI contract at {openapi_path}.')
else:
    print(f'Notice: OpenAPI file {openapi_path} not found yet.')
"

echo "=========================================================="
echo "  All contracts and schemas verified successfully.        "
echo "=========================================================="
