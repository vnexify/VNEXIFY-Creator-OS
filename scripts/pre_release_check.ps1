<#
.SYNOPSIS
    VNEXIFY Creator OS DevSecOps Pre-Release Automation Check

.DESCRIPTION
    Runs the complete 4-tier pre-release verification pipeline in sequence:
    1. security_scan.ps1 (Secret & Key Scanning)
    2. gitignore_audit.ps1 (.gitignore Exclusion Audit)
    3. health.ps1 (13-Point System Health Diagnostics)
    4. build.ps1 (React Frontend, Electron Shell, FastAPI Backend Build & Imports)

.EXAMPLE
    .\scripts\pre_release_check.ps1
#>

[CmdletBinding()]
param ()

$ErrorActionPreference = "Stop"

Write-Host "====================================================" -ForegroundColor Cyan
Write-Host "   VNEXIFY Creator OS - Pre-Release Security Check   " -ForegroundColor Cyan
Write-Host "====================================================" -ForegroundColor Cyan

# 1. Security Scan
Write-Host "`n[STAGE 1/4] Running Security Secret Scan (security_scan.ps1)..." -ForegroundColor Yellow
if (Test-Path ".\scripts\security_scan.ps1") {
    powershell -ExecutionPolicy Bypass -File ".\scripts\security_scan.ps1"
    if ($LASTEXITCODE -ne 0) {
        Write-Host "`n[FAIL] Pre-Release Stage 1 (Security Scan) Failed." -ForegroundColor Red
        exit $LASTEXITCODE
    }
} else {
    Write-Host "[ERROR] scripts/security_scan.ps1 not found." -ForegroundColor Red
    exit 1
}

# 2. GitIgnore Audit
Write-Host "`n[STAGE 2/4] Running GitIgnore Security Audit (gitignore_audit.ps1)..." -ForegroundColor Yellow
if (Test-Path ".\scripts\gitignore_audit.ps1") {
    powershell -ExecutionPolicy Bypass -File ".\scripts\gitignore_audit.ps1"
    if ($LASTEXITCODE -ne 0) {
        Write-Host "`n[FAIL] Pre-Release Stage 2 (GitIgnore Audit) Failed." -ForegroundColor Red
        exit $LASTEXITCODE
    }
} else {
    Write-Host "[ERROR] scripts/gitignore_audit.ps1 not found." -ForegroundColor Red
    exit 1
}

# 3. System Health Check
Write-Host "`n[STAGE 3/4] Running System Health Diagnostics (health.ps1)..." -ForegroundColor Yellow
if (Test-Path ".\scripts\health.ps1") {
    powershell -ExecutionPolicy Bypass -File ".\scripts\health.ps1"
    if ($LASTEXITCODE -ne 0) {
        Write-Host "`n[FAIL] Pre-Release Stage 3 (System Health) Failed." -ForegroundColor Red
        exit $LASTEXITCODE
    }
} else {
    Write-Host "[ERROR] scripts/health.ps1 not found." -ForegroundColor Red
    exit 1
}

# 4. Multi-Tier Build Verification
Write-Host "`n[STAGE 4/4] Running Multi-Tier Build Verification (build.ps1)..." -ForegroundColor Yellow
if (Test-Path ".\scripts\build.ps1") {
    powershell -ExecutionPolicy Bypass -File ".\scripts\build.ps1"
    if ($LASTEXITCODE -ne 0) {
        Write-Host "`n[FAIL] Pre-Release Stage 4 (Build Verification) Failed." -ForegroundColor Red
        exit $LASTEXITCODE
    }
} else {
    Write-Host "[ERROR] scripts/build.ps1 not found." -ForegroundColor Red
    exit 1
}

# Final Summary
Write-Host "`n====================================================" -ForegroundColor Green
Write-Host "         VNEXIFY PRE-RELEASE CHECK PASSED           " -ForegroundColor Green
Write-Host "====================================================" -ForegroundColor Green
exit 0
