# VNEXIFY Creator OS Git Security Hooks Guide

- **Version**: v1.1
- **Creation Date**: 2026-08-07
- **Role**: Principal DevSecOps & Git Security Engineer
- **Installer Script**: `scripts/install_git_hooks.ps1`
- **Target Hooks**: `.git/hooks/pre-commit`, `.git/hooks/pre-push`

---

## Table of Contents

- [1. Overview](#1-overview)
- [2. Pre-Commit Hook Specification](#2-pre-commit-hook-specification)
- [3. Pre-Push Hook Specification](#3-pre-push-hook-specification)
- [4. How Hooks Work](#4-how-hooks-work)
- [5. How to Reinstall Hooks](#5-how-to-reinstall-hooks)
- [6. Troubleshooting](#6-troubleshooting)

---

# 1. Overview

This document specifies the official **Git Security Hooks Automation** for **VNEXIFY Creator OS**. Git hooks operate as local client-side security gates, blocking commits containing exposed credentials and preventing pushes that fail pre-release verification.

---

# 2. Pre-Commit Hook Specification

- **Hook Path**: `.git/hooks/pre-commit`
- **Trigger**: Runs automatically before `git commit` finalizes.
- **Action**: Executes `scripts/security_scan.ps1`.
- **Pass Criteria**: Exit Code 0 ➔ Commit proceeds normally.
- **Fail Criteria**: Exit Code 1 ➔ Blocks commit and displays:
  ```text
  ===================================
  COMMIT BLOCKED
  Sensitive information detected.
  Remove the secret before committing.
  ===================================
  ```

---

# 3. Pre-Push Hook Specification

- **Hook Path**: `.git/hooks/pre-push`
- **Trigger**: Runs automatically before `git push` transmits commits to remote repositories.
- **Action**: Executes `scripts/pre_release_check.ps1` (6-Stage Pipeline).
- **Pass Criteria**: Exit Code 0 ➔ Push proceeds normally.
- **Fail Criteria**: Exit Code 1 ➔ Blocks push and displays:
  ```text
  ===================================
  PUSH BLOCKED
  Project failed verification.
  ===================================
  ```

---

# 4. How Hooks Work

1. `git commit` invokes `.git/hooks/pre-commit`.
2. `.git/hooks/pre-commit` calls PowerShell to run `scripts/security_scan.ps1`.
3. If any hardcoded API key, private key, token, or forbidden credential file is detected, the script returns exit code 1, which signals Git to abort the commit operation.
4. Similarly, `git push` invokes `.git/hooks/pre-push` to run the full pre-release verification pipeline (`security_scan` ➔ `gitignore_audit` ➔ `github_security_check` ➔ `gitleaks` ➔ `health` ➔ `build`).

---

# 5. How to Reinstall Hooks

The hook installer is safe to run multiple times. Reinstall hooks anytime by running:
```powershell
.\scripts\install_git_hooks.ps1
```

Console Output:
```text
====================================================
   VNEXIFY Creator OS - Install Git Security Hooks   
====================================================

[1/2] Installing pre-commit hook...
  [OK] pre-commit hook installed to .git/hooks/pre-commit
[2/2] Installing pre-push hook...
  [OK] pre-push hook installed to .git/hooks/pre-push

====================================================
         Git Security Hooks Installed Pass          
====================================================
```

---

# 6. Troubleshooting

- **Permissions on Linux/macOS**:
  If hooks fail with permission denied, make them executable:
  ```bash
  chmod +x .git/hooks/pre-commit .git/hooks/pre-push
  ```
- **Bypassing Hooks (Emergency Only)**:
  Use `--no-verify` ONLY during critical incident response under security architect approval.
