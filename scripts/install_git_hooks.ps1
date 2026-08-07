<#
.SYNOPSIS
    VNEXIFY Creator OS Git Hooks Installer Script

.DESCRIPTION
    Installs enterprise pre-commit and pre-push Git hooks into .git/hooks/
    to enforce automated secret scanning and pre-release verification gates.

.EXAMPLE
    .\scripts\install_git_hooks.ps1
#>

[CmdletBinding()]
param ()

$ErrorActionPreference = "Stop"

Write-Host "====================================================" -ForegroundColor Cyan
Write-Host "   VNEXIFY Creator OS - Install Git Security Hooks   " -ForegroundColor Cyan
Write-Host "====================================================" -ForegroundColor Cyan

$gitHooksDir = ".git/hooks"

if (-not (Test-Path ".git")) {
    Write-Host "[FAIL] Installation Failed: Not inside a Git repository root." -ForegroundColor Red
    exit 1
}

if (-not (Test-Path $gitHooksDir)) {
    New-Item -ItemType Directory -Path $gitHooksDir -Force | Out-Null
}

# 1. Install Pre-Commit Hook
Write-Host "`n[1/2] Installing pre-commit hook..." -ForegroundColor Yellow
$preCommitSrc = "scripts/hooks/pre-commit"
$preCommitDst = "$gitHooksDir/pre-commit"

if (Test-Path $preCommitSrc) {
    Copy-Item -Path $preCommitSrc -Destination $preCommitDst -Force
    Write-Host "  [OK] pre-commit hook installed to $preCommitDst" -ForegroundColor Green
} else {
    Write-Host "  [FAIL] Missing template: $preCommitSrc" -ForegroundColor Red
    exit 1
}

# 2. Install Pre-Push Hook
Write-Host "[2/2] Installing pre-push hook..." -ForegroundColor Yellow
$prePushSrc = "scripts/hooks/pre-push"
$prePushDst = "$gitHooksDir/pre-push"

if (Test-Path $prePushSrc) {
    Copy-Item -Path $prePushSrc -Destination $prePushDst -Force
    Write-Host "  [OK] pre-push hook installed to $prePushDst" -ForegroundColor Green
} else {
    Write-Host "  [FAIL] Missing template: $prePushSrc" -ForegroundColor Red
    exit 1
}

Write-Host "`n====================================================" -ForegroundColor Green
Write-Host "         Git Security Hooks Installed Pass          " -ForegroundColor Green
Write-Host "====================================================" -ForegroundColor Green
exit 0
