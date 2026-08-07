<#
.SYNOPSIS
    VNEXIFY Creator OS DevSecOps Pre-Release Automation Pipeline

.DESCRIPTION
    Runs the full 6-stage pre-release verification pipeline in sequence:
    1. security_scan.ps1 (Secret & Entropy Scanning)
    2. gitignore_audit.ps1 (.gitignore Rule Audit)
    3. github_security_check.ps1 (GitHub Security Audit)
    4. run_gitleaks.ps1 (Gitleaks Engine Scan)
    5. health.ps1 (13-Point System Health Diagnostics)
    6. build.ps1 (React Frontend, Electron Shell, FastAPI Backend Build & Imports)

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
Write-Host "`n[STAGE 1/6] Running Security Secret & Entropy Scan (security_scan.ps1)..." -ForegroundColor Yellow
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
Write-Host "`n[STAGE 2/6] Running GitIgnore Security Audit (gitignore_audit.ps1)..." -ForegroundColor Yellow
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

# 3. GitHub Security Check
Write-Host "`n[STAGE 3/6] Running GitHub Security Policy Audit (github_security_check.ps1)..." -ForegroundColor Yellow
if (Test-Path ".\scripts\github_security_check.ps1") {
    powershell -ExecutionPolicy Bypass -File ".\scripts\github_security_check.ps1"
    if ($LASTEXITCODE -ne 0) {
        Write-Host "`n[FAIL] Pre-Release Stage 3 (GitHub Security Check) Failed." -ForegroundColor Red
        exit $LASTEXITCODE
    }
} else {
    Write-Host "[ERROR] scripts/github_security_check.ps1 not found." -ForegroundColor Red
    exit 1
}

# 4. Gitleaks Scan
Write-Host "`n[STAGE 4/6] Running Gitleaks Engine Secret Detection (run_gitleaks.ps1)..." -ForegroundColor Yellow
if (Test-Path ".\scripts\run_gitleaks.ps1") {
    powershell -ExecutionPolicy Bypass -File ".\scripts\run_gitleaks.ps1"
    if ($LASTEXITCODE -ne 0) {
        Write-Host "`n[FAIL] Pre-Release Stage 4 (Gitleaks Scan) Failed." -ForegroundColor Red
        exit $LASTEXITCODE
    }
} else {
    Write-Host "[ERROR] scripts/run_gitleaks.ps1 not found." -ForegroundColor Red
    exit 1
}

# 5. System Health Check
Write-Host "`n[STAGE 5/6] Running System Health Diagnostics (health.ps1)..." -ForegroundColor Yellow
if (Test-Path ".\scripts\health.ps1") {
    powershell -ExecutionPolicy Bypass -File ".\scripts\health.ps1"
    if ($LASTEXITCODE -ne 0) {
        Write-Host "`n[FAIL] Pre-Release Stage 5 (System Health) Failed." -ForegroundColor Red
        exit $LASTEXITCODE
    }
} else {
    Write-Host "[ERROR] scripts/health.ps1 not found." -ForegroundColor Red
    exit 1
}

# 6. Multi-Tier Build Verification
Write-Host "`n[STAGE 6/6] Running Multi-Tier Build Verification (build.ps1)..." -ForegroundColor Yellow
if (Test-Path ".\scripts\build.ps1") {
    powershell -ExecutionPolicy Bypass -File ".\scripts\build.ps1"
    if ($LASTEXITCODE -ne 0) {
        Write-Host "`n[FAIL] Pre-Release Stage 6 (Build Verification) Failed." -ForegroundColor Red
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
