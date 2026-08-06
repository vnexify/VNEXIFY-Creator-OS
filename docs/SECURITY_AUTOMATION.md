# VNEXIFY Creator OS DevSecOps Security Automation Guide

- **Version**: v1.0
- **Creation Date**: 2026-08-06
- **Role**: Senior DevSecOps Engineer
- **Target Scripts**: `scripts/security_scan.ps1`, `scripts/gitignore_audit.ps1`, `scripts/pre_release_check.ps1`

---

## Table of Contents

- [1. Overview](#1-overview)
- [2. DevSecOps Security Automation Layer](#2-devsecops-security-automation-layer)
- [3. Script 1: `security_scan.ps1`](#3-script-1-security_scanps1)
- [4. Script 2: `gitignore_audit.ps1`](#4-script-2-gitignore_auditps1)
- [5. Script 3: `pre_release_check.ps1`](#5-script-3-pre_release_checkps1)
- [6. Execution & Console Outputs](#6-execution--console-outputs)

---

# 1. Overview

This guide details the **DevSecOps Security Automation Layer** for **VNEXIFY Creator OS**. Designed to protect cloud credits, developer identity, and private keys, these automated scripts audit source code, inspect `.gitignore` rules, and execute pre-release security verification before any release pipeline runs.

---

# 2. DevSecOps Security Automation Layer

```
[Developer / AI Agent]
          │
          ▼
┌───────────────────────────────────────────────────────────┐
│              scripts/pre_release_check.ps1                │
│                                                           │
│  [1/4] security_scan.ps1 ───► Scans source for secrets   │
│  [2/4] gitignore_audit.ps1 ─► Verifies exclusion rules   │
│  [3/4] health.ps1 ──────────► Verifies 13 health checks   │
│  [4/4] build.ps1 ───────────► Builds Frontend, Shell, App │
└─────────────────────────────┬─────────────────────────────┘
                              │
                              ├── [FAIL] ➔ Stop immediately, Exit 1
                              └── [PASS] ➔ VNEXIFY PRE-RELEASE CHECK PASSED
```

---

# 3. Script 1: `security_scan.ps1`

Performs static regex pattern auditing across `frontend/`, `backend/`, `electron/`, `scripts/`, and `docs/`, excluding `node_modules/`, `dist/`, `.venv/`, and `.git/`.

### Verified Secret Signatures
- **AI Keys**: OpenAI (`sk-proj-`), Gemini/Google (`AIzaSy`), Claude/Anthropic (`sk-ant-`), HuggingFace (`hf_`).
- **Cloud & Auth**: AWS (`AKIA`), GitHub PATs (`ghp_`, `github_pat_`), Stripe (`sk_live_`), Razorpay (`rzp_live_`).
- **Private Keys**: PEM Headers (`-----BEGIN PRIVATE KEY-----`).
- **Forbidden Credential Files**: `credentials.json`, `service-account.json`, `firebase-adminsdk.json`, `token.json`, `oauth.json`.

---

# 4. Script 2: `gitignore_audit.ps1`

Audits `.gitignore` to ensure protection for 25 mandatory secret, certificate, key, credential, build artifact, cache, and editor patterns:
- `.env`, `.env.*`, `!.env.example`
- `*.pem`, `*.key`, `*.crt`, `*.cer`, `*.p12`, `*.pfx`
- `credentials.json`, `service-account.json`, `firebase-adminsdk.json`, `secret.json`, `secrets.json`, `token.json`, `oauth.json`
- `.vscode/`, `.idea/`, `__pycache__/`, `*.pyc`, `.pytest_cache/`, `.mypy_cache/`
- `npm-debug.log*`, `yarn-error.log*`, `pnpm-debug.log*`

---

# 5. Script 3: `pre_release_check.ps1`

Integrates the full DevSecOps pipeline into a single pre-release automation gate executing in sequence:
1. `security_scan.ps1`
2. `gitignore_audit.ps1`
3. `health.ps1`
4. `build.ps1`

---

# 6. Execution & Console Outputs

From PowerShell terminal at repository root:
```powershell
.\scripts\pre_release_check.ps1
```

### Expected Output
```text
====================================================
   VNEXIFY Creator OS - Pre-Release Security Check   
====================================================

[STAGE 1/4] Running Security Secret Scan (security_scan.ps1)...
SECURITY SCAN PASSED

[STAGE 2/4] Running GitIgnore Security Audit (gitignore_audit.ps1)...
GitIgnore Audit Passed

[STAGE 3/4] Running System Health Diagnostics (health.ps1)...
System Healthy

[STAGE 4/4] Running Multi-Tier Build Verification (build.ps1)...
Build Successful!

====================================================
         VNEXIFY PRE-RELEASE CHECK PASSED           
====================================================
```
