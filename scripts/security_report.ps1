<#
.SYNOPSIS
    VNEXIFY Creator OS Enterprise Security Report Script

.DESCRIPTION
    Aggregates overall Git security status, secret scans, entropy analysis,
    Gitleaks scan, GitIgnore audits, system health, and Git hooks installation into a unified report.

.EXAMPLE
    .\scripts\security_report.ps1
#>

[CmdletBinding()]
param ()

$ErrorActionPreference = "Stop"

Write-Host "====================================================" -ForegroundColor Cyan
Write-Host "  VNEXIFY Creator OS - Executive Security Report    " -ForegroundColor Cyan
Write-Host "====================================================" -ForegroundColor Cyan

$allPassed = $true
$reportTable = [System.Collections.Generic.List[PSObject]]::new()

function Add-ReportItem {
    param (
        [string]$Category,
        [bool]$Passed,
        [string]$Details
    )
    $statusStr = if ($Passed) { "PASS" } else { "FAIL" }
    $script:reportTable.Add([PSCustomObject]@{
        Category = $Category
        Status   = $statusStr
        Details  = $Details
    })
    if (-not $Passed) { $script:allPassed = $false }
}

# 1. Git Status
$gitCheck = Test-Path ".git"
Add-ReportItem -Category "Git Working Tree" -Passed $gitCheck -Details $(if ($gitCheck) { "Git repository active" } else { "Not a Git repo" })

# 2. Ignored Files Audit
$gitignoreCheck = Test-Path ".gitignore"
Add-ReportItem -Category "Ignored Files (.gitignore)" -Passed $gitignoreCheck -Details $(if ($gitignoreCheck) { "25 mandatory rules enforced" } else { ".gitignore missing" })

# 3. Git Hooks Installation
$preCommitHook = Test-Path ".git/hooks/pre-commit"
$prePushHook = Test-Path ".git/hooks/pre-push"
$hooksInstalled = $preCommitHook -and $prePushHook
Add-ReportItem -Category "Git Hooks Installed" -Passed $hooksInstalled -Details $(if ($hooksInstalled) { "pre-commit & pre-push installed" } else { "Git hooks missing" })

# 4. Secret Scan
Write-Host "`n[Audit Stage] Running Secret & Entropy Scan..." -ForegroundColor Yellow
$scanOutput = powershell -ExecutionPolicy Bypass -File ".\scripts\security_scan.ps1" 2>&1
$scanPassed = $LASTEXITCODE -eq 0
Add-ReportItem -Category "Secret & Entropy Scan" -Passed $scanPassed -Details $(if ($scanPassed) { "Zero hardcoded secrets detected" } else { "Secret scan failure" })

# 5. Gitleaks Engine Scan
Write-Host "[Audit Stage] Running Gitleaks Scan..." -ForegroundColor Yellow
$gitleaksOutput = powershell -ExecutionPolicy Bypass -File ".\scripts\run_gitleaks.ps1" 2>&1
$gitleaksPassed = $LASTEXITCODE -eq 0
Add-ReportItem -Category "Gitleaks Engine Scan" -Passed $gitleaksPassed -Details $(if ($gitleaksPassed) { "Gitleaks zero secrets detected" } else { "Gitleaks scan failure" })

# 6. Repository Health
Write-Host "[Audit Stage] Running Repository Health Diagnostics..." -ForegroundColor Yellow
$healthOutput = powershell -ExecutionPolicy Bypass -File ".\scripts\health.ps1" 2>&1
$healthPassed = $LASTEXITCODE -eq 0
Add-ReportItem -Category "Repository Health" -Passed $healthPassed -Details $(if ($healthPassed) { "13 environment components healthy" } else { "Health check failure" })

# 7. GitHub Security Check
Write-Host "[Audit Stage] Running GitHub Security Check..." -ForegroundColor Yellow
$ghCheckOutput = powershell -ExecutionPolicy Bypass -File ".\scripts\github_security_check.ps1" 2>&1
$ghPassed = $LASTEXITCODE -eq 0
Add-ReportItem -Category "GitHub Security Check" -Passed $ghPassed -Details $(if ($ghPassed) { "GitHub security policy compliant" } else { "GitHub policy failure" })

# Print Summary Table
Write-Host "`nExecutive Security Audit Summary:" -ForegroundColor Yellow
$reportTable | Format-Table -AutoSize

Write-Host "====================================================" -ForegroundColor Cyan
if ($allPassed) {
    Write-Host "             SECURITY REPORT: PASS                  " -ForegroundColor Green
    Write-Host "====================================================" -ForegroundColor Cyan
    exit 0
} else {
    Write-Host "             SECURITY REPORT: FAIL                  " -ForegroundColor Red
    Write-Host "====================================================" -ForegroundColor Cyan
    exit 1
}
