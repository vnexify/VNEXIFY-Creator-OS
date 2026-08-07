# VNEXIFY Creator OS CI Pipeline Technical Manual

- **Version**: v1.0
- **Creation Date**: 2026-08-07
- **Role**: Principal DevOps & GitHub Actions Architect
- **Pipeline Definition**: [.github/workflows/ci.yml](file:///c:/Users/viren/OneDrive/Desktop/VNEXIFY/.github/workflows/ci.yml)

---

## Table of Contents

- [1. Pipeline Stage Matrix](#1-pipeline-stage-matrix)
- [2. Detailed Stage Breakdown](#2-detailed-stage-breakdown)
- [3. Failure Handling & Exit Conditions](#3-failure-handling--exit-conditions)
- [4. Success Markers](#4-success-markers)

---

# 1. Pipeline Stage Matrix

The CI pipeline executes 11 sequential stages on every push and pull request:

| Stage | Name | Executable / Action | Pass Criteria |
| :---: | :--- | :--- | :--- |
| **1** | Checkout Repository | `actions/checkout@v4` | Full repository checkout complete |
| **2** | Setup Node.js | `actions/setup-node@v4` | Node.js 20.x runtime active |
| **3** | Setup Python | `actions/setup-python@v5` | Python 3.11.x runtime active |
| **4** | Install npm Dependencies | `npm ci` | Hoisted dependencies installed clean |
| **5** | Install Python Dependencies | `pip install -r backend/requirements.txt` | Virtualenv active with requirements |
| **6** | Security Secret Scan | `scripts/security_scan.ps1` | Zero secrets or sensitive variable leaks |
| **7** | GitIgnore Audit | `scripts/gitignore_audit.ps1` | All secret rules present in `.gitignore` |
| **8** | GitHub Security Audit | `scripts/github_security_check.ps1` | Zero sensitive extensions in Git index |
| **9** | Gitleaks Engine Scan | `scripts/run_gitleaks.ps1` | Zero Gitleaks repository findings |
| **10** | System Health Diagnostics | `scripts/health.ps1` | All 13 system components return PASS |
| **11** | Multi-Tier Build Check | `scripts/build.ps1` | React, Electron, and FastAPI build PASS |

---

# 2. Detailed Stage Breakdown

### Stages 1–5: Environment Initialization
- **Stage 1 (Checkout)**: Retrieves complete Git history (`fetch-depth: 0`) required for Gitleaks entropy analysis.
- **Stage 2 & 3 (Tooling Setup)**: Prepares Node.js 20 and Python 3.11 runtimes with caching enabled.
- **Stage 4 & 5 (Dependencies)**: Installs npm packages (`npm ci`) and Python backend virtualenv dependencies cleanly.

### Stages 6–9: DevSecOps Verification Layer
- **Stage 6 (`security_scan.ps1`)**: Audits Git staged index and workspace for 17 token regexes and Shannon entropy ($H > 4.8$). Emits `✓ Security Passed`.
- **Stage 7 (`gitignore_audit.ps1`)**: Audits `.gitignore` rules. Emits `✓ GitIgnore Passed`.
- **Stage 8 (`github_security_check.ps1`)**: Audits untracked `.env`, `.env.example`, and tracked file extensions. Emits `✓ GitHub Security Passed`.
- **Stage 9 (`run_gitleaks.ps1`)**: Runs Gitleaks detection while ignoring bundled third-party files. Emits `✓ Gitleaks Passed`.

### Stages 10–11: Diagnostics & Multi-Tier Build Layer
- **Stage 10 (`health.ps1`)**: Verifies 13 core framework components. Emits `✓ Health Passed`.
- **Stage 11 (`build.ps1`)**: Compiles React frontend (`tsc && vite build`), Electron shell (`npx tsc`), and validates Python FastAPI imports. Emits `✓ Build Passed` followed by `CI SUCCESS`.

---

# 3. Failure Handling & Exit Conditions

The pipeline enforces strict fail-fast behavior:
- Any step returning exit code $\ne 0$ halts execution immediately.
- The pipeline displays standard failure diagnostic tables pinpointing the failing line or component.

---

# 4. Success Markers

When all 11 stages pass cleanly, the pipeline logs the following summary:
```text
✓ Security Passed
✓ GitIgnore Passed
✓ GitHub Security Passed
✓ Gitleaks Passed
✓ Health Passed
✓ Build Passed

====================================================
                    CI SUCCESS                      
====================================================
```
