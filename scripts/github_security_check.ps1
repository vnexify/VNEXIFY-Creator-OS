<#
.SYNOPSIS
    VNEXIFY Creator OS GitHub Security Audit Script

.DESCRIPTION
    Audits repository configuration to ensure strict compliance with the
    Official GitHub Security Policy: validates untracked status of .env,
    presence of .env.example, .gitignore rules, and tracked file extensions.

.EXAMPLE
    .\scripts\github_security_check.ps1
#>

[CmdletBinding()]
param ()

$ErrorActionPreference = "Stop"

Write-Host "====================================================" -ForegroundColor Cyan
Write-Host "  VNEXIFY Creator OS - GitHub Security Audit Check  " -ForegroundColor Cyan
Write-Host "====================================================" -ForegroundColor Cyan

# Safe Git Command Discovery
$gitExe = Get-Command "git" -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Source
if (-not $gitExe -and (Test-Path "C:\Program Files\Git\cmd\git.exe")) {
    $gitExe = "C:\Program Files\Git\cmd\git.exe"
}

$allPassed = $true

# 1. Verify .gitignore existence
Write-Host "`n[1/5] Verifying .gitignore file..." -ForegroundColor Yellow
if (Test-Path ".gitignore") {
    Write-Host "  [OK] .gitignore exists" -ForegroundColor Green
} else {
    Write-Host "  [FAIL] Missing .gitignore file" -ForegroundColor Red
    $allPassed = $false
}

# 2. Verify .env file untracked status
Write-Host "[2/5] Verifying .env environment file status..." -ForegroundColor Yellow
if (Test-Path ".env") {
    $isEnvTracked = $false
    if ($gitExe) {
        $trackedEnv = (& $gitExe ls-files .env 2>$null)
        if (-not [string]::IsNullOrWhiteSpace($trackedEnv)) {
            $isEnvTracked = $true
        }
    }
    if ($isEnvTracked) {
        Write-Host "  [FAIL] .env is TRACKED in Git repository!" -ForegroundColor Red
        $allPassed = $false
    } else {
        Write-Host "  [OK] .env exists locally and is NOT tracked by Git" -ForegroundColor Green
    }
} else {
    Write-Host "  [INFO] .env file does not exist locally (Using runtime defaults)" -ForegroundColor Cyan
}

# 3. Verify .env.example template file
Write-Host "[3/5] Verifying .env.example template file..." -ForegroundColor Yellow
if (Test-Path ".env.example") {
    Write-Host "  [OK] .env.example exists" -ForegroundColor Green
} else {
    Write-Host "  [FAIL] Missing .env.example template file" -ForegroundColor Red
    $allPassed = $false
}

# 4. Check for tracked sensitive file extensions in Git
Write-Host "[4/5] Auditing Git tracked files for sensitive extensions..." -ForegroundColor Yellow
$sensitiveExtensions = @("*.pem", "*.key", "*.crt", "*.cer", "*.p12", "*.pfx", "credentials.json", "service-account.json", "firebase-adminsdk.json", "token.json", "oauth.json")

$trackedSecretsFound = $false
if ($gitExe) {
    $trackedFiles = (& $gitExe ls-files 2>$null)
    foreach ($ext in $sensitiveExtensions) {
        $pattern = [regex]::Escape($ext).Replace('\*', '.*')
        $matches = $trackedFiles | Where-Object { $_ -match "^$pattern$" -or $_ -match "/$pattern$" }
        if ($matches) {
            Write-Host "  [FAIL] Tracked sensitive file in Git: $($matches[0])" -ForegroundColor Red
            $trackedSecretsFound = $true
            $allPassed = $false
        }
    }
}

if (-not $trackedSecretsFound) {
    Write-Host "  [OK] Zero tracked secret files/certificates found in Git index" -ForegroundColor Green
}

# 5. Check Git Working Tree Status
Write-Host "[5/5] Checking Git repository working tree status..." -ForegroundColor Yellow
if ($gitExe) {
    $statusOutput = (& $gitExe status --porcelain 2>$null)
    if ([string]::IsNullOrWhiteSpace($statusOutput)) {
        Write-Host "  [OK] Git working tree is clean" -ForegroundColor Green
    } else {
        Write-Host "  [INFO] Git working tree has modified/untracked files" -ForegroundColor Cyan
    }
}

Write-Host "`n====================================================" -ForegroundColor Cyan
if ($allPassed) {
    Write-Host "         GitHub Security Check PASSED               " -ForegroundColor Green
    Write-Host "====================================================" -ForegroundColor Cyan
    exit 0
} else {
    Write-Host "         GitHub Security Check FAILED               " -ForegroundColor Red
    Write-Host "====================================================" -ForegroundColor Cyan
    exit 1
}
