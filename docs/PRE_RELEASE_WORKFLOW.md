# VNEXIFY Creator OS Pre-Release Automation Workflow Guide

- **Version**: v1.0
- **Creation Date**: 2026-08-06
- **Role**: Senior DevSecOps Engineer
- **Target Pipeline**: `scripts/pre_release_check.ps1` ➔ `scripts/release.ps1`

---

## Table of Contents

- [1. Overview](#1-overview)
- [2. Pre-Release Pipeline Architecture](#2-pre-release-pipeline-architecture)
- [3. Sequential Stages & Exit Criteria](#3-sequential-stages--exit-criteria)
- [4. Developer Checklist Before Release](#4-developer-checklist-before-release)
- [5. Remediation for Pipeline Failures](#5-remediation-for-pipeline-failures)

---

# 1. Overview

This document specifies the official **Pre-Release Automation Workflow for VNEXIFY Creator OS**. Prior to committing tag releases or executing `scripts/release.ps1`, developers and release engineers MUST execute `scripts/pre_release_check.ps1` to ensure zero secret leaks, verified `.gitignore` rules, 100% environment health, and clean multi-tier builds.

---

# 2. Pre-Release Pipeline Architecture

```
[Developer / Release Engineer]
             │
             ▼
   .\scripts\pre_release_check.ps1
             │
             ├── [STAGE 1] security_scan.ps1 (Secret & Key Scanning)
             │      └── FAIL ➔ Exit 1
             │
             ├── [STAGE 2] gitignore_audit.ps1 (.gitignore Rule Audit)
             │      └── FAIL ➔ Exit 1
             │
             ├── [STAGE 3] health.ps1 (13-Point System Health Checks)
             │      └── FAIL ➔ Exit 1
             │
             ├── [STAGE 4] build.ps1 (React Frontend + Electron + Backend)
             │      └── FAIL ➔ Exit 1
             │
             └── [PASS] ➔ Display "VNEXIFY PRE-RELEASE CHECK PASSED"
                        │
                        ▼
            .\scripts\release.ps1 (Git Commit & Release Tagging)
```

---

# 3. Sequential Stages & Exit Criteria

| Stage # | Script Name | Verification Target | Pass Condition |
| :--- | :--- | :--- | :--- |
| **Stage 1** | `security_scan.ps1` | Scans for tracked `.env`, hardcoded API keys, private keys, certs, credential JSON files | `SECURITY SCAN PASSED` (Exit 0) |
| **Stage 2** | `gitignore_audit.ps1` | Audits `.gitignore` for 25 mandatory exclusion patterns | `GitIgnore Audit Passed` (Exit 0) |
| **Stage 3** | `health.ps1` | Diagnoses Git repo, Python `.venv`, Node/npm, modules, directories (`logs`, `exports`, `docs`, `backend/db`) | `System Healthy` (Exit 0) |
| **Stage 4** | `build.ps1` | Builds React frontend (`npm run build:frontend`), typechecks Electron shell (`npx tsc`), tests FastAPI backend imports | `Build Successful!` (Exit 0) |

---

# 4. Developer Checklist Before Release

1. Confirm all feature work is complete and tested.
2. Confirm `.env` file is NOT staged in Git (`git status`).
3. Run `.\scripts\pre_release_check.ps1`.
4. Verify console output displays `VNEXIFY PRE-RELEASE CHECK PASSED`.
5. Proceed to run `.\scripts\release.ps1`.

---

# 5. Remediation for Pipeline Failures

- **If Stage 1 Fails**: Remove hardcoded API key or private key from source files. Move secret to `.env`.
- **If Stage 2 Fails**: Add missing pattern to `.gitignore`.
- **If Stage 3 Fails**: Run `npm install` or ensure Python `.venv` is activated.
- **If Stage 4 Fails**: Fix TypeScript compilation or React Vite build errors.
