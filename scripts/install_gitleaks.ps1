<#
.SYNOPSIS
    VNEXIFY Creator OS Gitleaks Automated Installer Script

.DESCRIPTION
    Verifies if Gitleaks binary is installed on PATH or in scripts/bin/gitleaks.exe.
    If missing, automatically downloads and extracts the standalone Gitleaks executable
    for Windows 64-bit to provide zero-config secret scanning.

.EXAMPLE
    .\scripts\install_gitleaks.ps1
#>

[CmdletBinding()]
param ()

$ErrorActionPreference = "Stop"

Write-Host "====================================================" -ForegroundColor Cyan
Write-Host "   VNEXIFY Creator OS - Install Gitleaks Security   " -ForegroundColor Cyan
Write-Host "====================================================" -ForegroundColor Cyan

# 1. Check if Gitleaks is on system PATH
$gitleaksCmd = Get-Command "gitleaks" -ErrorAction SilentlyContinue
if ($gitleaksCmd) {
    $ver = (& gitleaks version 2>&1)
    Write-Host "[OK] Gitleaks detected on system PATH." -ForegroundColor Green
    Write-Host "     Version: $ver" -ForegroundColor Green
    exit 0
}

# 2. Check if Gitleaks exists in local scripts/bin/ directory
$binDir = "scripts/bin"
$localGitleaks = "$binDir/gitleaks.exe"

if (Test-Path $localGitleaks) {
    $ver = (& $localGitleaks version 2>&1)
    Write-Host "[OK] Gitleaks detected in local workspace ($localGitleaks)." -ForegroundColor Green
    Write-Host "     Version: $ver" -ForegroundColor Green
    exit 0
}

# 3. Download standalone Gitleaks executable for Windows x64
Write-Host "`n[INFO] Gitleaks not found. Downloading portable binary..." -ForegroundColor Yellow

if (-not (Test-Path $binDir)) {
    New-Item -ItemType Directory -Path $binDir -Force | Out-Null
}

$gitleaksUrl = "https://github.com/gitleaks/gitleaks/releases/download/v8.18.4/gitleaks_8.18.4_windows_x64.zip"
$zipPath = "$binDir/gitleaks.zip"

try {
    Write-Host "Downloading Gitleaks release v8.18.4 from GitHub..." -ForegroundColor Yellow
    [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12
    Invoke-WebRequest -Uri $gitleaksUrl -OutFile $zipPath -UseBasicParsing

    Write-Host "Extracting Gitleaks executable to $binDir..." -ForegroundColor Yellow
    Expand-Archive -Path $zipPath -DestinationPath $binDir -Force
    Remove-Item -Path $zipPath -Force -ErrorAction SilentlyContinue

    if (Test-Path $localGitleaks) {
        $ver = (& $localGitleaks version 2>&1)
        Write-Host "`n====================================================" -ForegroundColor Green
        Write-Host "     Gitleaks Installed Successfully (v$ver)        " -ForegroundColor Green
        Write-Host "====================================================" -ForegroundColor Green
        exit 0
    } else {
        Write-Host "[FAIL] Extraction completed but $localGitleaks not found." -ForegroundColor Red
        exit 1
    }
} catch {
    Write-Host "[WARNING] Automatic download failed. Attempting winget package manager fallback..." -ForegroundColor Yellow
    $wingetCmd = Get-Command "winget" -ErrorAction SilentlyContinue
    if ($wingetCmd) {
        try {
            winget install --id gitleaks.gitleaks -e --accept-source-agreements --accept-package-agreements
            if (Get-Command "gitleaks" -ErrorAction SilentlyContinue) {
                Write-Host "[OK] Gitleaks installed via winget." -ForegroundColor Green
                exit 0
            }
        } catch {}
    }
    
    Write-Host "[FAIL] Could not automatically install Gitleaks: $_" -ForegroundColor Red
    exit 1
}
