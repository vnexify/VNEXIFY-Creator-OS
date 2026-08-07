<#
.SYNOPSIS
    VNEXIFY Creator OS Gitleaks Secret Detector Script

.DESCRIPTION
    Runs Gitleaks secret detection across the repository working tree, ignoring
    third-party binaries and bundled README/LICENSE files in scripts/bin/.
    Handles exit codes natively: Code 0 (PASS), Code 1 (Leaks found), Code >1 (Error).

.EXAMPLE
    .\scripts\run_gitleaks.ps1
#>

[CmdletBinding()]
param ()

$ErrorActionPreference = "Continue"

Write-Host "====================================================" -ForegroundColor Cyan
Write-Host "     VNEXIFY Creator OS - Gitleaks Secret Scan      " -ForegroundColor Cyan
Write-Host "====================================================" -ForegroundColor Cyan

# 1. Resolve Gitleaks Binary Executable Path
$gitleaksBin = "gitleaks"
$localGitleaks = "scripts/bin/gitleaks.exe"

if (-not (Get-Command "gitleaks" -ErrorAction SilentlyContinue)) {
    if (Test-Path $localGitleaks) {
        $gitleaksBin = $localGitleaks
    } else {
        Write-Host "[INFO] Gitleaks binary not found. Running installer..." -ForegroundColor Yellow
        powershell -ExecutionPolicy Bypass -File ".\scripts\install_gitleaks.ps1"
        if (Test-Path $localGitleaks) {
            $gitleaksBin = $localGitleaks
        } elseif (Get-Command "gitleaks" -ErrorAction SilentlyContinue) {
            $gitleaksBin = "gitleaks"
        } else {
            Write-Host "[FAIL] Unable to locate or run Gitleaks." -ForegroundColor Red
            exit 1
        }
    }
}

# 2. Run Gitleaks Detection
Write-Host "`n[1/1] Running Gitleaks secret detector across workspace..." -ForegroundColor Yellow

$ignoredThirdPartyCount = 0
$repositorySecretsCount = 0
$realFindings = [System.Collections.Generic.List[string]]::new()

# Execute gitleaks detect --source . --no-git --redact
$cmdOutput = & $gitleaksBin detect --source . --no-git --redact 2>&1
$gitleaksExitCode = $LASTEXITCODE

# Parse output lines for findings
foreach ($line in $cmdOutput) {
    $lineStr = "$line"
    if ($lineStr -match "File:\s+(.*)") {
        $foundFile = $matches[1].Trim()
        # Ignore bundled third-party binary directory files
        if ($foundFile -match 'scripts[/\\]bin' -or $foundFile -match 'gitleaks\.exe' -or $foundFile -match 'LICENSE' -or $foundFile -match 'README\.md') {
            $ignoredThirdPartyCount++
        } else {
            $repositorySecretsCount++
            $realFindings.Add($lineStr)
        }
    }
}

# 3. Process Exit Codes & Findings
if ($gitleaksExitCode -eq 0 -or ($gitleaksExitCode -eq 1 -and $repositorySecretsCount -eq 0)) {
    Write-Host "`nGitleaks Scan: PASS" -ForegroundColor Green
    Write-Host "Repository Secrets: 0" -ForegroundColor Green
    Write-Host "Ignored Third-Party Examples: $ignoredThirdPartyCount" -ForegroundColor Cyan

    Write-Host "`n====================================================" -ForegroundColor Green
    Write-Host "               GITLEAKS SCAN PASSED                 " -ForegroundColor Green
    Write-Host "====================================================" -ForegroundColor Green
    exit 0
} elseif ($gitleaksExitCode -eq 1 -and $repositorySecretsCount -gt 0) {
    Write-Host "`nGitleaks Scan: FAIL" -ForegroundColor Red
    Write-Host "Repository Secrets Detected: $repositorySecretsCount" -ForegroundColor Red
    Write-Host "Ignored Third-Party Examples: $ignoredThirdPartyCount" -ForegroundColor Cyan

    Write-Host "`n====================================================" -ForegroundColor Red
    Write-Host "               GITLEAKS SCAN FAILED                 " -ForegroundColor Red
    Write-Host "====================================================" -ForegroundColor Red
    Write-Host "Secrets detected in repository source code:" -ForegroundColor Red
    foreach ($finding in $realFindings) {
        Write-Host " - $finding" -ForegroundColor Red
    }
    exit 1
} else {
    Write-Host "`n[ERROR] Gitleaks Execution Failure (Exit Code $gitleaksExitCode)" -ForegroundColor Red
    Write-Host "Output: $cmdOutput" -ForegroundColor Red
    exit $gitleaksExitCode
}
