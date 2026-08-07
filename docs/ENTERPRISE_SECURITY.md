# VNEXIFY Creator OS Enterprise Security Architecture

- **Version**: v1.1
- **Creation Date**: 2026-08-07
- **Role**: Principal DevSecOps & Git Security Engineer

---

## Table of Contents

- [1. Executive Overview](#1-executive-overview)
- [2. Secret Handling & Environment Isolation](#2-secret-handling--environment-isolation)
- [3. Incident Response Protocol](#3-incident-response-protocol)
- [4. Credential Rotation Procedures](#4-credential-rotation-procedures)
- [5. Developer Security Checklist](#5-developer-security-checklist)
- [6. Git Best Practices](#6-git-best-practices)
- [7. GitHub Security Best Practices](#7-github-security-best-practices)

---

# 1. Executive Overview

This document defines the **Enterprise Security Architecture** for **VNEXIFY Creator OS**. As a local-first desktop application integrating generative AI services (OpenAI, Gemini, Claude) and SQLite persistence, protecting cloud provider billing, API credentials, and client data is a top-level architectural requirement.

---

# 2. Secret Handling & Environment Isolation

1. **Zero Hardcoded Secrets Policy**: API keys, JWT secrets, OAuth secrets, database credentials, and SSL private keys must NEVER be stored in source code files or documentation.
2. **Local Environment Injection**: Secrets must be loaded exclusively via `.env` files using `pydantic-settings` in `backend/app/core/config.py`.
3. **Template Standardization**: All sample configuration keys must use explicit placeholder strings inside `.env.example`.

---

# 3. Incident Response Protocol

If an API key or private credential is accidentally exposed or committed:

```
                  ┌─────────────────────────────────────┐
                  │      SECRET EXPOSURE DETECTED       │
                  └──────────────────┬──────────────────┘
                                     │
                                     ▼
                  ┌─────────────────────────────────────┐
                  │ Execute scripts/rotate_secret_check │
                  └──────────────────┬──────────────────┘
                                     │
         ┌───────────────────────────┴───────────────────────────┐
         ▼                                                       ▼
┌─────────────────────────────────┐             ┌─────────────────────────────────┐
│ 1. REVOKE EXPOSED KEY IN CLOUD  │             │ 2. GENERATE NEW KEY IN DASHBOARD│
└────────────────┬────────────────┘             └────────────────┬────────────────┘
                 │                                               │
                 └───────────────────────┬───────────────────────┘
                                         │
                                         ▼
                        ┌─────────────────────────────────┐
                        │ 3. UPDATE LOCAL .env FILE       │
                        └─────────────────────────────────┘
```

---

# 4. Credential Rotation Procedures

Execute the automated remediation helper:
```powershell
.\scripts\rotate_secret_check.ps1 -SecretType "OpenAI API Key"
```

Follow the provider dashboard direct links provided by the script to revoke the compromised token immediately and issue a replacement key.

---

# 5. Developer Security Checklist

- [ ] `.env` is listed in `.gitignore` and untracked by Git (`git status`).
- [ ] Git security hooks are installed (`.\scripts\install_git_hooks.ps1`).
- [ ] Gitleaks scanner is installed & verified (`.\scripts\install_gitleaks.ps1`).
- [ ] Pre-release verification passes (`.\scripts\pre_release_check.ps1`).
- [ ] Executive security audit report passes (`.\scripts\security_report.ps1`).

---

# 6. Git Best Practices

- Always run `git status` before `git add` to ensure no `.env` or credential files are staged.
- Keep commits small, atomic, and well-described.
- Ensure `.git/hooks/pre-commit` and `.git/hooks/pre-push` are active locally.

---

# 7. GitHub Security Best Practices

- Enable **GitHub Secret Scanning** and **Dependabot Security Updates** on the remote repository.
- Enforce branch protection rules requiring status checks and signed commits on `main`.
- Enforce mandatory `.gitignore` protection for `.env`, `*.pem`, `*.key`, `credentials.json`, `service-account.json`, etc.
