# VNEXIFY Creator OS DevOps & Security Automation Guide

- **Version**: v1.0
- **Creation Date**: 2026-08-06
- **Role**: Senior DevSecOps Engineer

---

## Table of Contents

- [1. Overview](#1-overview)
- [2. Automation Script Suite](#2-automation-script-suite)
- [3. Pre-Release Verification Pipeline](#3-pre-release-verification-pipeline)
- [4. Release Automation Workflow](#4-release-automation-workflow)
- [5. System Health Diagnostics](#5-system-health-diagnostics)

---

# 1. Overview

This document serves as the master guide for **VNEXIFY Creator OS DevOps & Security Automation**. It details the automated PowerShell script suite spanning health diagnostics, multi-tier build verification, secret scanning, `.gitignore` auditing, pre-release gates, and release tagging.

---

# 2. Automation Script Suite

| Script Name | Path | Purpose & Function |
| :--- | :--- | :--- |
| `security_scan.ps1` | [scripts/security_scan.ps1](file:///c:/Users/viren/OneDrive/Desktop/VNEXIFY/scripts/security_scan.ps1) | Scans workspace for hardcoded secrets, API keys, private keys, certs, credential JSON files. |
| `gitignore_audit.ps1` | [scripts/gitignore_audit.ps1](file:///c:/Users/viren/OneDrive/Desktop/VNEXIFY/scripts/gitignore_audit.ps1) | Audits `.gitignore` for 25 mandatory secret, key, cert, credential, log, editor, and cache patterns. |
| `health.ps1` | [scripts/health.ps1](file:///c:/Users/viren/OneDrive/Desktop/VNEXIFY/scripts/health.ps1) | Executes 13-point environment diagnostic health check and renders health table. |
| `build.ps1` | [scripts/build.ps1](file:///c:/Users/viren/OneDrive/Desktop/VNEXIFY/scripts/build.ps1) | Builds React frontend (`npm run build:frontend`), typechecks Electron, verifies FastAPI imports. |
| `pre_release_check.ps1` | [scripts/pre_release_check.ps1](file:///c:/Users/viren/OneDrive/Desktop/VNEXIFY/scripts/pre_release_check.ps1) | Runs 4-tier pre-release pipeline (`security_scan` ➔ `gitignore_audit` ➔ `health` ➔ `build`). |
| `release.ps1` | [scripts/release.ps1](file:///c:/Users/viren/OneDrive/Desktop/VNEXIFY/scripts/release.ps1) | Automates Git status checks, staging, conventional release commits, and version tagging. |

---

# 3. Pre-Release Verification Pipeline

Run the pre-release check before triggering releases:
```powershell
.\scripts\pre_release_check.ps1
```

If all 4 stages pass, output displays `VNEXIFY PRE-RELEASE CHECK PASSED`.

---

# 4. Release Automation Workflow

Execute release script only after `pre_release_check.ps1` returns exit code 0:
```powershell
.\scripts\release.ps1
```
