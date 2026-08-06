# VNEXIFY Creator OS Security Guidelines & Policy

- **Version**: v1.0
- **Status**: Official Security & GitHub Protection Policy
- **Creation Date**: 2026-08-06

---

## Table of Contents

- [1. Overview](#1-overview)
- [2. GitHub Security Policy & Secret Protection](#2-github-security-policy--secret-protection)
- [3. Security Principles](#3-security-principles)
- [4. Dependency Security](#4-dependency-security)
- [5. Data & Local Persistence Security](#5-data--local-persistence-security)
- [6. Environment Security](#6-environment-security)
- [7. Related Documents](#7-related-documents)

---

# 1. Overview

This document outlines security considerations for VNEXIFY Creator OS, including dependencies, environment management, secrets isolation, and GitHub data protection.

---

# 2. GitHub Security Policy & Secret Protection

> [!CAUTION]
> NO secrets, credentials, API keys, tokens, or private certificates may EVER be committed to Git or pushed to GitHub.

All developers and AI assistants MUST strictly follow the 10 Non-Negotiable Rules detailed in [GITHUB_SECURITY_POLICY.md](GITHUB_SECURITY_POLICY.md):
1. **Never Hardcode Secrets**: Keep API keys, tokens, passwords, and private keys out of source files, markdown, and logs.
2. **Environment Variables**: Load secrets dynamically at runtime from `.env` via `pydantic-settings`.
3. **Placeholder Template**: Maintain `.env.example` with ONLY placeholder strings (`OPENAI_API_KEY=your_api_key_here`).
4. **Git Exclusions**: Ensure `.gitignore` explicitly protects `.env`, `.env.*`, `*.pem`, `*.key`, `credentials.json`, `service-account.json`, etc.
5. **Zero-Token Commits**: Never stage or commit credentials or secrets.
6. **Automated Stop Gate**: If a secret is detected, HALT execution immediately and generate a Security Warning.
7. **No Secret Echoing**: Never print secret values in logs, reports, or terminal outputs.
8. **Pre-Release Verification**: Run security audits before release.
9. **Universal Compliance**: Every AI assistant and tool MUST obey this policy.
10. **Immediate Remediation**: Never save or repeat exposed keys; immediately move them to `.env` and rotate/revoke them.

---

# 3. Security Principles

- Minimize risk by using proven, audited dependencies.
- Keep sensitive data out of source control.
- Verify runtime environment configurations before starting services.

---

# 4. Dependency Security

- Audit npm and Python packages before installation.
- Avoid deprecated or unmaintained dependencies.
- Track approved package versions in `TECH_STACK.md` and `BACKLOG.md`.

---

# 5. Data & Local Persistence Security

- Use local-first SQLite stored at `backend/db/vnexify.db`.
- Secure runtime settings using `.env` files.
- Validate and sanitize all API input parameters using Pydantic models.

---

# 6. Environment Security

- Use isolated Python virtual environments (`.venv/`).
- Keep editor and terminal settings local to the workspace.
- Validate package installs before using them.

---

# 7. Related Documents

- [GITHUB_SECURITY_POLICY.md](GITHUB_SECURITY_POLICY.md)
- [PROJECT_RULES.md](PROJECT_RULES.md)
- [AI_INSTRUCTIONS.md](AI_INSTRUCTIONS.md)
- [DEVELOPMENT_WORKFLOW.md](DEVELOPMENT_WORKFLOW.md)
