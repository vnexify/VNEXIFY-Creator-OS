# VNEXIFY Creator OS Build Automation Guide

- Version: v0.1
- Creation Date: 2026-08-06
- Role: DevOps Build Engineer
- Target Script: `scripts/build.ps1`

---

## Table of Contents

- [1. Overview](#1-overview)
- [2. Multi-Tier Verification Steps](#2-multi-tier-verification-steps)
- [3. Dynamic Dependency Detection](#3-dynamic-dependency-detection)
- [4. Usage & Command Examples](#4-usage--command-examples)
- [5. Expected Console Output](#5-expected-console-output)
- [6. Error Handling & Exit Codes](#6-error-handling--exit-codes)

---

# 1. Overview

The `scripts/build.ps1` script provides a unified build automation and verification system for **VNEXIFY Creator OS**. It validates system dependencies, dynamically detects npm workspace node_modules configurations, compiles the React frontend bundle, typechecks the Electron desktop shell, and tests FastAPI backend module importability.

---

# 2. Multi-Tier Verification Steps

```
[START] ➔ [Step 1] Verify Project Root (package.json, electron, backend)
          │
          ├── [Step 2] Verify Node.js & npm (node --version, npm --version)
          │
          ├── [Step 3] Verify Python Virtual Environment (.venv/Scripts/python.exe)
          │
          ├── [Step 4] Verify npm Dependencies Dynamically (Root / Frontend / Hoisted)
          │     ├── [Missing Everywhere] ➔ Print "[FAIL] npm node_modules missing" ➔ Exit 1
          │     └── [Detected] ➔ Print "npm Dependencies: PASS"
          │
          ├── [Step 5] Build React Frontend (npm run build:frontend)
          │     ├── [FAIL] ➔ Stop immediately, Exit $LASTEXITCODE
          │     └── [PASS] ➔ Print "Frontend PASS"
          │
          ├── [Step 6] Compile Electron Shell (npx tsc --project electron/tsconfig.json)
          │     ├── [FAIL] ➔ Stop immediately, Exit $LASTEXITCODE
          │     └── [PASS] ➔ Print "Electron PASS"
          │
          ├── [Step 7] Verify Backend Imports (python -c "from backend.app.main import app")
          │     ├── [FAIL] ➔ Stop immediately, Exit $LASTEXITCODE
          │     └── [PASS] ➔ Print "Backend PASS"
          │
          └── [SUCCESS] ➔ Print "Build Successful!" ➔ Exit 0
```

---

# 3. Dynamic Dependency Detection

`scripts/build.ps1` dynamically detects dependency installation across three supported project configurations:
1. **Root Workspace**: `node_modules/` (npm hoisted).
2. **Frontend Workspace**: `frontend/node_modules/`.
3. **Installed Packages**: `node_modules/react` or `frontend/node_modules/react`.

If dependencies exist in any valid location, the build proceeds.

---

# 4. Usage & Command Examples

From PowerShell terminal at repository root:
```powershell
.\scripts\build.ps1
```

---

# 5. Expected Console Output

```text
====================================================
     VNEXIFY Creator OS - Build Automation System    
====================================================

[1/7] Verifying project root environment...
[2/7] Verifying Node.js & npm environment...
Node.js: v20.11.0 | npm: 10.2.4

[3/7] Verifying Python virtual environment...
Python Venv: Python 3.14.4

[4/7] Verifying npm dependencies...
npm Dependencies: PASS (Root & Frontend Workspaces)

[5/7] Building React Frontend (npm run build:frontend)...
> tsc && vite build
✓ 56 modules transformed.
Frontend PASS

[6/7] Compiling Electron Shell (npx tsc --project electron/tsconfig.json)...
Electron PASS

[7/7] Verifying FastAPI Backend Imports...
Backend app module loaded successfully
Backend PASS

====================================================
                Build Successful!                   
====================================================
```

---

# 6. Error Handling & Exit Codes

| Exit Code | Cause | Behavior |
| :--- | :--- | :--- |
| `0` | All verification & build stages passed | Prints `Build Successful!` and exits 0. |
| `1` | Dependencies missing everywhere | Prints `[FAIL] npm node_modules directory missing. Please run 'npm install'.` |
| `$LASTEXITCODE` | Build failure in Frontend, Electron, or Backend | Halts immediately without hiding native error trace. |
