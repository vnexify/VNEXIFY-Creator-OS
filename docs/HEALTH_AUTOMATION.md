# VNEXIFY Creator OS Health Automation Guide

- Version: v0.1
- Creation Date: 2026-08-06
- Role: DevOps Health Engineer
- Target Script: `scripts/health.ps1`

---

## Table of Contents

- [1. Overview](#1-overview)
- [2. Dynamic Workspace Detection](#2-dynamic-workspace-detection)
- [3. Health Diagnostic Checks](#3-health-diagnostic-checks)
- [4. Usage & Execution](#4-usage--execution)
- [5. Expected Console Output](#5-expected-console-output)

---

# 1. Overview

The `scripts/health.ps1` script provides a single-command health diagnostic tool for **VNEXIFY Creator OS**. It inspects 13 core environment components, workspace directories, dependency trees, and build artifacts, displaying a clean PowerShell table and summary verdict (`System Healthy` or `System Issues Detected`).

---

# 2. Dynamic Workspace Detection

`scripts/health.ps1` features dynamic detection for `node_modules` across workspace configurations:
- **Root Workspace (Hoisted)**: `node_modules/`
- **Frontend Workspace**: `frontend/node_modules/`
- **Installed Packages**: `node_modules/react`

If dependencies exist in any valid location, the check yields `PASS`. If dependencies are missing everywhere, it yields `FAIL`.

---

# 3. Health Diagnostic Checks

| Check # | Component | Verification Rule | Expected Status |
| :--- | :--- | :--- | :--- |
| **1** | Git Repository | `git rev-parse --is-inside-work-tree` | Git repository detected |
| **2** | Python Venv | `.\.venv\Scripts\python.exe` existence & version | Python 3.14+ |
| **3** | Node.js Tooling | `node --version` | Node.js v20+ |
| **4** | npm Package Mgr | `npm --version` | npm v10+ |
| **5** | Frontend Modules | Dynamic detection across root & frontend | PASS (Workspaces detected) |
| **6** | Backend Modules | Imports `fastapi`, `sqlalchemy`, `pydantic` in `.venv` | Dependencies verified |
| **7** | Electron Config | `electron/tsconfig.json` & electron modules | Shell config present |
| **8** | SQLite Directory | `backend/db` directory existence | Directory present |
| **9** | Logs Directory | `logs` directory existence | Directory present |
| **10** | Exports Directory | `exports` directory existence | Directory present |
| **11** | Docs Directory | `docs` directory existence | Directory present |
| **12** | Frontend Dist | `frontend/dist` bundle directory | Build bundle present |
| **13** | Backend DB Path | `backend/db` directory path | Path verified |

---

# 4. Usage & Execution

From PowerShell terminal at repository root:
```powershell
.\scripts\health.ps1
```

---

# 5. Expected Console Output

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
Frontend Modules   PASS   Root & Frontend Workspaces present
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
