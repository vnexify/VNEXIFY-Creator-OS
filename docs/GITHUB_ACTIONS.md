# VNEXIFY Creator OS GitHub Actions Workflow Guide

- **Version**: v1.0
- **Creation Date**: 2026-08-07
- **Role**: Principal DevOps & GitHub Actions Architect
- **Target File**: [.github/workflows/ci.yml](file:///c:/Users/viren/OneDrive/Desktop/VNEXIFY/.github/workflows/ci.yml)

---

## Table of Contents

- [1. Overview](#1-overview)
- [2. Workflow Triggers & Execution Scope](#2-workflow-triggers--execution-scope)
- [3. Enterprise Security & Secret Protection](#3-enterprise-security--secret-protection)
- [4. Runner Environment Specifications](#4-runner-environment-specifications)
- [5. Troubleshooting CI Failures](#5-troubleshooting-ci-failures)

---

# 1. Overview

VNEXIFY Creator OS incorporates an Enterprise Grade GitHub Actions CI pipeline designed to enforce automated verification on every commit, pull request, and release branch. The workflow directly mirrors the local `scripts/pre_release_check.ps1` pipeline, ensuring strict parity between developer workstations and continuous integration runners.

---

# 2. Workflow Triggers & Execution Scope

The CI pipeline defined in [.github/workflows/ci.yml](file:///c:/Users/viren/OneDrive/Desktop/VNEXIFY/.github/workflows/ci.yml) triggers automatically under the following conditions:

- **Push Events**:
  - `main` branch
  - `master` branch
  - `develop` branch
  - `release/**` feature/release branches
- **Pull Request Events**:
  - Target branches: `main`, `master`, `develop`

---

# 3. Enterprise Security & Secret Protection

- **Zero Secrets Logged**: The pipeline executes static analysis (`security_scan.ps1`) and Gitleaks (`run_gitleaks.ps1`) without exposing tokens, passwords, JWT, or API keys in standard output or workflow logs.
- **Read-Only Token Permissions**: The workflow operates under strict `permissions: contents: read` scoping to prevent unauthorized modifications to repository resources.
- **Automated Commit Gate**: Pull requests containing hardcoded credentials or unmasked tokens are blocked automatically during Stage 6 (Security Scan) and Stage 9 (Gitleaks Scan).

---

# 4. Runner Environment Specifications

| Parameter | Specification | Description |
| :--- | :--- | :--- |
| **Operating System** | `windows-latest` | Native PowerShell execution environment matching Windows 11 desktop shell |
| **Node.js Runtime** | Node.js `20.x` | Hoisted npm workspace dependency resolution |
| **Python Runtime** | Python `3.11.x` | FastAPI backend dependencies & virtual environment isolation |
| **Shell Type** | `powershell` | PowerShell 7+ script orchestration |

---

# 5. Troubleshooting CI Failures

If a CI step fails:
1. Inspect the GitHub Actions run summary for the specific failing stage (e.g. Stage 6 Security Scan or Stage 11 Build).
2. Reproduce the failure locally on your workstation by running:
   ```powershell
   .\scripts\pre_release_check.ps1
   ```
3. Fix the underlying code or secret violation before re-pushing your commit or updating the pull request.
