# VNEXIFY Creator OS Official GitHub Security Policy

- **Version**: v1.0
- **Status**: Official & Permanent Security Policy
- **Creation Date**: 2026-08-06
- **Scope**: Mandatory for all Developers, AI Assistants, Multi-Agent Frameworks, and CI/CD Automation

---

## Table of Contents

- [1. Overview](#1-overview)
- [2. Non-Negotiable Security Rules](#2-non-negotiable-security-rules)
- [3. Protected Secret Types](#3-protected-secret-types)
- [4. Environment Variables & `.env.example`](#4-environment-variables--envexample)
- [5. Git Ignore & Exclusion Standards](#5-git-ignore--exclusion-standards)
- [6. Incident Response & Accidental Exposure Remediation](#6-incident-response--accidental-exposure-remediation)
- [7. AI Safety & Agent Security Enforcement](#7-ai-safety--agent-security-enforcement)
- [8. Pre-Release Security Audit Gate](#8-pre-release-security-audit-gate)

---

# 1. Overview

This document establishes the **Official GitHub Security Policy for VNEXIFY Creator OS**. As a local-first desktop application designed for AI integration, this repository will be hosted on public and private GitHub repositories. To protect developer identity, cloud resource credits, and infrastructure integrity, **NO secrets, credentials, API keys, or private certificates may EVER be committed to Git**.

This security policy is **PERMANENT** and binding for all future development sprints.

---

# 2. Non-Negotiable Security Rules

> [!CAUTION]
> The following 10 Security Rules are non-negotiable and strictly enforced across all toolsets and AI agents.

### RULE 1: Never Hardcode Secrets
Never place raw credentials, keys, or tokens inside source code (`frontend/`, `electron/`, `backend/`), configuration files, tests, documentation, or scripts.

### RULE 2: Mandatory Use of Environment Variables
All secret values MUST be loaded dynamically at runtime via environment variables (`.env`). Secrets MUST NEVER appear in documentation, markdown, reports, logs, code examples, or terminal outputs.

### RULE 3: Strict `.env.example` Template Standard
Maintain `.env.example` at repository root containing **ONLY clean placeholder strings** (e.g. `OPENAI_API_KEY=your_openai_api_key_here`). Real credential values are strictly forbidden inside `.env.example`.

### RULE 4: Git Ignore Exclusion Enforcement
The `.gitignore` file MUST explicitly exclude `.env`, `.env.*`, `*.pem`, `*.key`, `*.crt`, `*.cer`, `*.p12`, `*.pfx`, `credentials.json`, `service-account.json`, `firebase-adminsdk.json`, `secret.json`, `secrets.json`, `token.json`, and `oauth.json`.

### RULE 5: Zero-Token Git Commit Policy
Never stage or commit `.env`, API keys, passwords, certificates, service credentials, tokens, or RSA/PEM private keys into any Git branch.

### RULE 6: Automated Exposure Stop Gate
If any secret or API key pattern is detected inside the workspace or staged files, **STOP immediately**, generate a high-priority Security Warning, halt implementation, and DO NOT commit or push to Git.

### RULE 7: Zero Secret Printing in Logs & Reports
Secrets MUST NEVER be echoed or printed inside terminal outputs, log files (`logs/backend.log`), markdown documentation, changelogs, or sprint reports.

### RULE 8: Pre-Release Security Verification
Before every release, run a security audit confirming:
- No secrets staged in Git.
- No API keys hardcoded in source.
- `.gitignore` is valid and active.
- `.env` is ignored by Git.

### RULE 9: Universal AI Assistant Compliance
Every AI assistant (ChatGPT, Antigravity, Google AI Studio, Stitch, Ollama, Copilot, Claude, Gemini, Cursor, Windsurf, Codex) MUST obey this policy. No AI is permitted to bypass these rules.

### RULE 10: Accidental Credential Exposure Remediation
If a developer accidentally pastes a credential into chat or code:
- **Do NOT save it.**
- **Do NOT repeat or echo it in output.**
- **Immediately recommend moving it to `.env` and revoking/replacing the exposed key.**

---

# 3. Protected Secret Types

The following secret types must NEVER be committed to Git:

- **AI Provider Keys**: OpenAI API Keys, Gemini API Keys, Google AI Studio Keys, Claude / Anthropic Keys, HuggingFace Tokens, Ollama private configs.
- **Authentication & JWT**: JWT Secrets, Session Secrets, OAuth Client Secrets, Encryption Keys, RSA/PEM Keys, Private Certificates (`*.pem`, `*.key`, `*.crt`).
- **Cloud & Infrastructure**: AWS Access/Secret Keys, Azure Storage Keys, GCP Credentials (`credentials.json`, `service-account.json`), Firebase Admin SDK JSON files (`firebase-adminsdk.json`).
- **Database & Services**: Database Passwords, SMTP Mail Credentials, Redis Passwords.
- **Developer & Third-Party Tokens**: GitHub Personal Access Tokens, Discord Tokens, Telegram Bot Tokens, Stripe/Razorpay/PayPal API Keys.

---

# 4. Environment Variables & `.env.example`

Local development runtime configuration is managed via `.env` (ignored by Git) and modeled dynamically via `pydantic-settings` in `backend/app/core/config.py`.

### Authoritative `.env.example` Template
```ini
# Application & Host Settings
FASTAPI_ENV=development
FASTAPI_HOST=127.0.0.1
FASTAPI_PORT=8000
REACT_APP_API_URL=http://127.0.0.1:8000/api

# Database Configuration
DATABASE_URL=sqlite:///backend/db/vnexify.db

# Authentication & Tokens
JWT_SECRET=your_jwt_secret_key_here
SESSION_SECRET=your_session_secret_here

# AI Model Provider API Keys (Placeholders Only)
OPENAI_API_KEY=your_openai_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
CLAUDE_API_KEY=your_claude_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
HUGGINGFACE_TOKEN=your_huggingface_token_here
OLLAMA_BASE_URL=http://localhost:11434
```

---

# 5. Git Ignore & Exclusion Standards

The `.gitignore` at the project root enforces the following security exclusions:

```gitignore
# Environment files
.env
.env.*
!.env.example

# Certificates & Private Keys
*.pem
*.key
*.crt
*.cer
*.p12
*.pfx

# Secrets & Credentials
credentials.json
service-account.json
firebase-adminsdk.json
secret.json
secrets.json
token.json
oauth.json
```

---

# 6. Incident Response & Accidental Exposure Remediation

If a credential is accidentally committed or exposed in prompt history:
1. **Revoke Immediately**: Invalidate the compromised token at the provider console (e.g. OpenAI, GCP, GitHub).
2. **Purge Commit History**: Remove the credential from Git history using `git filter-repo` or BFG Repo-Cleaner.
3. **Rotate Key**: Issue a new credential and place it securely in local `.env`.

---

# 7. AI Safety & Agent Security Enforcement

All AI agents operating within this workspace MUST inspect `.gitignore` and source files before staging commits. If an AI agent detects a hardcoded secret:
- Halt task execution immediately.
- Notify the user with a `[SECURITY WARNING]` alert.
- Refuse to execute `git add` or `git commit` until the secret is removed.

---

# 8. Pre-Release Security Audit Gate

Prior to executing `scripts/release.ps1`, the build pipeline verifies:
1. `git status` reports `.env` as untracked/ignored.
2. Search regex for secret signatures (`sk-proj-`, `AIzaSy`, `ghp_`, `-----BEGIN PRIVATE KEY-----`) returns zero matches in tracked files.
3. `.env.example` contains only placeholder values.
