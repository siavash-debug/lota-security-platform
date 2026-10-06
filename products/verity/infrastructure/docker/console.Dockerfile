# ==============================================================================
# LOTA Security Verity - Web Console Dockerfile
# Production Hardened Frontend Scaffold
# NOTE: In production, pin exact SHA-256 digest: node:20-alpine@sha256:...
# NOTE: Release images must attach CycloneDX SBOM and SLSA Cosign signature.
# ==============================================================================

FROM node:20-alpine AS builder

WORKDIR /app

COPY package.json ./

# Safe install of dependencies
RUN npm install --ignore-scripts

COPY . .

# Build placeholder static/standalone assets
ENV NEXT_TELEMETRY_DISABLED=1

FROM node:20-alpine AS runner

WORKDIR /app

ENV NODE_ENV=production \
    PORT=3000

# Security: Run as unprivileged node user
USER node

COPY --from=builder /app/package.json ./package.json

EXPOSE 3000

CMD ["npm", "start"]
