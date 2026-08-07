# VNEXIFY Creator OS Gitleaks Security Guide

- **Version**: v1.0
- **Creation Date**: 2026-08-07
- **Role**: Principal DevSecOps & Git Security Engineer
- **Automated Installer**: `scripts/install_gitleaks.ps1`
- **Scanner Script**: `scripts/run_gitleaks.ps1`

---

## Table of Contents

- [1. Overview](#1-overview)
- [2. Automated Installation](#2-automated-installation)
- [3. Usage & Execution](#3-usage--execution)
- [4. Secret Detection Rules & Signatures](#4-secret-detection-rules--signatures)
- [5. Troubleshooting & FAQ](#5-troubleshooting--faq)

---

# 1. Overview

**Gitleaks** is an enterprise-grade SAST (Static Application Security Testing) tool designed to detect and prevent hardcoded secrets like passwords, API keys, JWT tokens, and private keys in Git repositories and working trees. In **VNEXIFY Creator OS**, Gitleaks runs automatically during pre-release checks (`scripts/pre_release_check.ps1`).

---

# 2. Automated Installation

To verify or automatically install Gitleaks without manual configuration, run:
```powershell
.\scripts\install_gitleaks.ps1
```

### Installation Logic
1. Checks if `gitleaks` exists on the system PATH.
2. If missing, checks for local binary `scripts/bin/gitleaks.exe`.
3. If still missing, automatically downloads the standalone Gitleaks Windows x64 release from GitHub into `scripts/bin/gitleaks.exe`.

---

# 3. Usage & Execution

Execute the standalone scanner script from PowerShell:
```powershell
.\scripts\run_gitleaks.ps1
```

### Console Output (Pass Example)
```text
====================================================
     VNEXIFY Creator OS - Gitleaks Secret Scan      
====================================================

[1/1] Running Gitleaks detect across repository...

====================================================
               GITLEAKS SCAN PASSED                 
====================================================
```

---

# 4. Secret Detection Rules & Signatures

Gitleaks audits source files for over 150 credential types, including:
- **Generative AI Keys**: OpenAI (`sk-proj-`), Google AI Studio (`AIzaSy`), Anthropic (`sk-ant-`).
- **Cloud Provider Credentials**: AWS Access Key IDs (`AKIA`), Azure Storage Account Keys, Google Cloud Service Account JSON.
- **Payment & SaaS Tokens**: Stripe (`sk_live_`), Razorpay, PayPal, GitHub PATs (`ghp_`), Slack, Discord, Telegram.
- **Certificates & Private Keys**: RSA, EC, OPENSSH, PEM headers (`-----BEGIN PRIVATE KEY-----`).

---

# 5. Troubleshooting & FAQ

- **Download Failure due to Firewall / Proxy**:
  If automatic download is blocked, install Gitleaks via package manager:
  ```powershell
  winget install gitleaks
  ```
  or copy `gitleaks.exe` manually into `scripts/bin/gitleaks.exe`.

- **False Positives in Documentation**:
  Whitelisted documentation and template files (`.env.example`) are automatically excluded from scanning.
