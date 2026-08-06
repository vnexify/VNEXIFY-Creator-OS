<#
.SYNOPSIS
    VNEXIFY Creator OS Build Automation Script

.DESCRIPTION
    Automates multi-tier build verification for VNEXIFY Creator OS:
    1. Verifies project root environment structure.
    2. Verifies Node.js & npm toolset.
    3. Verifies Python virtual environment (.venv).
    4. Dynamically detects npm dependencies (Root workspace, Frontend workspace, or Hoisted npm workspaces).
    5. Builds React frontend (npm run build:frontend).
    6. Compiles Electron TypeScript (npx tsc --project electron/tsconfig.json).
    7. Verifies FastAPI backend imports (from backend.app.main import app).

.EXAMPLE
    .\scripts\build.ps1
#>

[CmdletBinding()]
param ()

$ErrorActionPreference = "Stop"

Write-Host "====================================================" -ForegroundColor Cyan
Write-Host "     VNEXIFY Creator OS - Build Automation System    " -ForegroundColor Cyan
Write-Host "====================================================" -ForegroundColor Cyan

# 1. Verify Project Root
Write-Host "`n[1/7] Verifying project root environment..." -ForegroundColor Yellow
if (-not (Test-Path "package.json") -or -not (Test-Path "frontend/package.json") -or -not (Test-Path "electron/tsconfig.json") -or -not (Test-Path "backend/app/main.py")) {
    Write-Host "[ERROR] Current directory is not the VNEXIFY Creator OS project root." -ForegroundColor Red
    exit 1
}

# 2. Verify Node.js & npm
Write-Host "`n[2/7] Verifying Node.js & npm environment..." -ForegroundColor Yellow
$nodeVersion = node --version 2>$null
$npmVersion = npm --version 2>$null
if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($nodeVersion)) {
    Write-Host "[ERROR] Node.js is not installed or not available on PATH." -ForegroundColor Red
    exit 1
}
Write-Host "Node.js: $nodeVersion | npm: $npmVersion" -ForegroundColor Gray

# 3. Verify Python Virtual Environment
Write-Host "`n[3/7] Verifying Python virtual environment..." -ForegroundColor Yellow
$venvPython = ".\.venv\Scripts\python.exe"
if (-not (Test-Path $venvPython)) {
    Write-Host "[ERROR] Python virtual environment not found at .venv/Scripts/python.exe." -ForegroundColor Red
    exit 1
}
$pyVersion = & $venvPython --version 2>&1
Write-Host "Python Venv: $pyVersion" -ForegroundColor Gray

# 4. Verify npm dependencies dynamically across workspace configurations
Write-Host "`n[4/7] Verifying npm dependencies..." -ForegroundColor Yellow
$rootModules = Test-Path "node_modules"
$frontendModules = Test-Path "frontend/node_modules"
$reactInstalled = (Test-Path "node_modules/react") -or (Test-Path "frontend/node_modules/react")

if ($rootModules -or $frontendModules -or $reactInstalled) {
    $detectedLocation = if ($rootModules -and $frontendModules) { "Root & Frontend Workspaces" } elseif ($rootModules) { "Root Workspace (Hoisted)" } else { "Frontend Workspace" }
    Write-Host "npm Dependencies: PASS ($detectedLocation)" -ForegroundColor Gray
} else {
    Write-Host "[FAIL] npm node_modules directory missing. Please run 'npm install'." -ForegroundColor Red
    exit 1
}

# 5. Build Frontend
Write-Host "`n[5/7] Building React Frontend (npm run build:frontend)..." -ForegroundColor Yellow
npm run build:frontend
if ($LASTEXITCODE -ne 0) {
    Write-Host "`n[FAIL] React Frontend Build Failed." -ForegroundColor Red
    exit $LASTEXITCODE
}
Write-Host "Frontend PASS" -ForegroundColor Green

# 6. Compile Electron
Write-Host "`n[6/7] Compiling Electron Shell (npx tsc --project electron/tsconfig.json)..." -ForegroundColor Yellow
npx tsc --project electron/tsconfig.json
if ($LASTEXITCODE -ne 0) {
    Write-Host "`n[FAIL] Electron Shell Compilation Failed." -ForegroundColor Red
    exit $LASTEXITCODE
}
Write-Host "Electron PASS" -ForegroundColor Green

# 7. Verify Backend Imports
Write-Host "`n[7/7] Verifying FastAPI Backend Imports..." -ForegroundColor Yellow
& $venvPython -c "from backend.app.main import app; print('Backend app module loaded successfully')" 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "`n[FAIL] Backend Module Import Verification Failed." -ForegroundColor Red
    exit $LASTEXITCODE
}
Write-Host "Backend PASS" -ForegroundColor Green

# Build Completion Summary
Write-Host "`n====================================================" -ForegroundColor Green
Write-Host "                Build Successful!                   " -ForegroundColor Green
Write-Host "====================================================" -ForegroundColor Green
exit 0
