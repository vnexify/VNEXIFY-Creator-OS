# VNEXIFY Creator OS Build Automation Guide

- Version: v0.1
- Creation Date: 2026-08-06
- Role: DevOps Build Engineer
- Target Script: `scripts/build.ps1`

---

## Table of Contents

- [1. Overview](#1-overview)
- [2. Multi-Tier Verification Steps](#2-multi-tier-verification-steps)
- [3. Usage & Command Examples](#3-usage--command-examples)
- [4. Expected Console Output](#4-expected-console-output)
- [5. Error Handling & Exit Codes](#5-error-handling--exit-codes)
- [6. Maintenance & CI Integration](#6-maintenance--ci-integration)

---

# 1. Overview

The `scripts/build.ps1` script provides a unified build automation and verification system for **VNEXIFY Creator OS**. It validates system dependencies, verifies environment roots, compiles the React frontend bundle, typechecks the Electron desktop shell, and tests FastAPI backend module importability.

---

# 2. Multi-Tier Verification Steps

```
[START] ➔ [Step 1] Verify Project Root (package.json, electron, backend)
          │
          ├── [Step 2] Verify Node.js & npm (node --version, npm --version)
          │
          ├── [Step 3] Verify Python Virtual Environment (.venv/Scripts/python.exe)
          │
          ├── [Step 4] Verify npm Node Modules (node_modules, frontend/node_modules)
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

# 3. Usage & Command Examples

### Executing Build Automation
From PowerShell terminal at the repository root:
```powershell
.\scripts\build.ps1
```

---

# 4. Expected Console Output

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

# 5. Error Handling & Exit Codes

| Exit Code | Cause | Behavior |
| :--- | :--- | :--- |
| `0` | All 7 verification & build stages passed | Prints `Build Successful!` and exits cleanly. |
| `1` | Invalid project directory | Prints `[ERROR] Current directory is not the VNEXIFY Creator OS project root.` |
| `1` | Missing Node.js or Python `.venv` | Prints toolchain missing error message and halts. |
| `$LASTEXITCODE` | Frontend, Electron, or Backend step fails | Prints `[FAIL] ... Failed.` and halts execution immediately. |

---

# 6. Maintenance & CI Integration

> [!TIP]
> Run `.\scripts\build.ps1` locally prior to submitting pull requests or running `.\scripts\release.ps1`.
