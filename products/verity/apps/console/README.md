# LOTA Security Verity - Web Console Scaffold

This directory houses the operator web interface scaffold for **LOTA Security Verity**.

---

## 1. Overview & Status

- **Product Title**: LOTA Security Verity
- **Subtitle**: Evidence-driven security posture assessment.
- **Mode**: Scaffolding Mode.
- **Implementation Status**: Frontend user interface scaffold only. No authentication is implemented, and no active network calls are made to backend endpoints.

---

## 2. Directory Structure

```text
console/
├── README.md               # This document
├── package.json            # Dependencies and Next.js scripts
├── public/                 # Static assets
└── src/
    ├── app/
    │   ├── layout.tsx      # Root application layout
    │   └── page.tsx        # Dashboard placeholder page
    ├── components/
    │   └── Card.tsx        # Dashboard card presentation component
    ├── lib/
    │   └── types.ts        # TypeScript interface definitions
    └── styles/
        └── globals.css     # Clean CSS styling
```

---

## 3. Local Installation & Development

To install dependencies and start the local development server:
```bash
npm install
npm run dev
```

The web console will be accessible at: `http://localhost:3000`.
