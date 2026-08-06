# VNEXIFY Creator OS Health Automation Guide

- Version: v0.1
- Creation Date: 2026-08-06
- Role: DevOps Health Engineer
- Target Script: `scripts/health.ps1`

---

## Table of Contents

- [1. Overview](#1-overview)
- [2. Health Diagnostic Checks](#2-health-diagnostic-checks)
- [3. Usage & Execution](#3-usage--execution)
- [4. Expected Console Output](#4-expected-console-output)
- [5. Troubleshooting & Remediation](#5-troubleshooting--remediation)

---

# 1. Overview

The `scripts/health.ps1` script provides a single-command health diagnostic tool for **VNEXIFY Creator OS**. It inspects 13 core environment components, workspace directories, dependency trees, and build artifacts, displaying a clean PowerShell table and summary verdict (`System Healthy` or `System Issues Detected`).

---

# 2. Health Diagnostic Checks

| Check # | Component | Verification Rule | Expected Status |
| :--- | :--- | :--- | :--- |
| **1** | Git Repository | `git rev-parse --is-inside-work-tree` | Git repository detected |
| **2** | Python Venv | `.\.venv\Scripts\python.exe` existence & version | Python 3.14+ |
| **3** | Node.js Tooling | `node --version` | Node.js v20+ |
| **4** | npm Package Mgr | `npm --version` | npm v10+ |
| **5** | Frontend Modules | `frontend/node_modules` existence | Directory present |
| **6** | Backend Modules | Imports `fastapi`, `sqlalchemy`, `pydantic` in `.venv` | Dependencies verified |
| **7** | Electron Config | `electron/tsconfig.json` & `node_modules/electron` | Shell config present |
| **8** | SQLite Directory | `backend/db` directory existence | Directory present |
| **9** | Logs Directory | `logs` directory existence | Directory present |
| **10** | Exports Directory | `exports` directory existence | Directory present |
| **11** | Docs Directory | `docs` directory existence | Directory present |
| **12** | Frontend Dist | `frontend/dist` bundle directory | Build bundle present |
| **13** | Backend DB Path | `backend/db` directory path | Path verified |

---

# 3. Usage & Execution

From PowerShell terminal at the repository root:
```powershell
.\scripts\health.ps1
```

---

# 4. Expected Console Output

```text
====================================================
     VNEXIFY Creator OS - System Health Diagnostics  
====================================================

System Diagnostics Table:

Component          Status Details
---------          ------ -------
Git Repository     PASS   Git repository detected
Python Venv        PASS   Python 3.14.4
Node.js Tooling    PASS   v20.11.0
npm Package Mgr    PASS   v10.2.4
Frontend Modules   PASS   frontend/node_modules present
Backend Modules    PASS   FastAPI, SQLAlchemy, Pydantic verified
Electron Config    PASS   Electron shell & tsconfig present
SQLite Directory   PASS   backend/db exists
Logs Directory     PASS   logs folder exists
Exports Directory  PASS   exports folder exists
Docs Directory     PASS   docs folder exists
Frontend Dist      PASS   frontend/dist bundle exists
Backend DB Path    PASS   backend/db path verified

====================================================
                System Healthy                      
====================================================
```

---

# 5. Troubleshooting & Remediation

- **If Backend Modules FAIL**: Run `.\.venv\Scripts\pip.exe install -r backend/requirements.txt`.
- **If Frontend Modules FAIL**: Run `npm install` from repository root.
- **If Frontend Dist FAILS**: Run `npm run build:frontend` or `.\scripts\build.ps1`.
