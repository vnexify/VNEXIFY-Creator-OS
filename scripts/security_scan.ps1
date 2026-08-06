<#
.SYNOPSIS
    VNEXIFY Creator OS DevSecOps Security Scan Script

.DESCRIPTION
    Scans the repository source code and documentation for hardcoded secrets,
    private keys, API tokens, certificates, and credential files prior to release.
    Compatible with PowerShell 5.1, PowerShell 7+, and Windows 11.

.EXAMPLE
    .\scripts\security_scan.ps1
#>

[CmdletBinding()]
param ()

$ErrorActionPreference = "Stop"

Write-Host "====================================================" -ForegroundColor Cyan
Write-Host "     VNEXIFY Creator OS - DevSecOps Security Scan    " -ForegroundColor Cyan
Write-Host "====================================================" -ForegroundColor Cyan

# 1. Verify tracked .env files in Git
Write-Host "`n[1/3] Auditing Git working tree for tracked secret files..." -ForegroundColor Yellow
if (Test-Path ".env") {
    $isEnvTracked = (git ls-files .env 2>$null)
    if (-not [string]::IsNullOrWhiteSpace($isEnvTracked)) {
        Write-Host "`n[FAIL] SECURITY SCAN FAILED" -ForegroundColor Red
        Write-Host "Detected tracked .env file in Git repository: .env" -ForegroundColor Red
        exit 1
    }
}

# 2. Audit restricted file patterns in workspace
Write-Host "[2/3] Checking workspace for forbidden credential files..." -ForegroundColor Yellow
$forbiddenFiles = @(
    "credentials.json",
    "service-account.json",
    "firebase-adminsdk.json",
    "secret.json",
    "secrets.json",
    "token.json",
    "oauth.json"
)

foreach ($f in $forbiddenFiles) {
    $found = Get-ChildItem -Path . -Recurse -Filter $f -ErrorAction SilentlyContinue | 
        Where-Object { $_.FullName -notmatch '\\(node_modules|dist|\.venv|\.git)\\' }
    
    if ($found) {
        Write-Host "`n[FAIL] SECURITY SCAN FAILED" -ForegroundColor Red
        Write-Host "Forbidden credential file detected: $($found[0].FullName)" -ForegroundColor Red
        exit 1
    }
}

# 3. Deep Regex Pattern Scanning across target directories
Write-Host "[3/3] Performing deep regex pattern scan for API keys & secrets..." -ForegroundColor Yellow

$targetDirs = @("frontend", "backend", "electron", "scripts", "docs")
$secretPatterns = @(
    @{ Name = "OpenAI API Key"; Pattern = "sk-proj-[a-zA-Z0-9_-]{20,}" },
    @{ Name = "Gemini / Google AI Studio Key"; Pattern = "AIzaSy[a-zA-Z0-9_-]{33}" },
    @{ Name = "Claude / Anthropic Key"; Pattern = "sk-ant-[a-zA-Z0-9_-]{20,}" },
    @{ Name = "HuggingFace Token"; Pattern = "hf_[a-zA-Z0-9]{34}" },
    @{ Name = "AWS Access Key"; Pattern = "AKIA[0-9A-Z]{16}" },
    @{ Name = "GitHub Personal Access Token"; Pattern = "ghp_[a-zA-Z0-9]{36}" },
    @{ Name = "GitHub Fine-Grained Token"; Pattern = "github_pat_[a-zA-Z0-9_-]{22,}" },
    @{ Name = "Stripe Live Key"; Pattern = "sk_live_[0-9a-zA-Z]{24}" },
    @{ Name = "Razorpay Live Key"; Pattern = "rzp_live_[0-9a-zA-Z]{14}" },
    @{ Name = "PEM Private Key Header"; Pattern = "-----BEGIN (RSA|EC|OPENSSH|PRIVATE) KEY-----" }
)

$suspiciousFound = $false
$failedFile = ""
$failedReason = ""

foreach ($dir in $targetDirs) {
    if (-not (Test-Path $dir)) { continue }
    
    $files = Get-ChildItem -Path $dir -Recurse -File -ErrorAction SilentlyContinue |
        Where-Object { 
            $_.FullName -notmatch '\\(node_modules|dist|\.venv|\.git|build|\.vite)\\' -and
            $_.Extension -notmatch '\.(png|jpg|jpeg|ico|gif|woff|woff2|ttf|eot|sqlite3|db)$'
        }

    foreach ($file in $files) {
        # Skip scanning documentation files that discuss security regex rules or script files containing regex patterns
        if ($file.Name -eq ".env.example" -or $file.Name -eq "security_scan.ps1" -or $file.Name -eq "GITHUB_SECURITY_POLICY.md" -or $file.Name -eq "SECURITY_AUTOMATION.md" -or $file.Name -eq "SECURITY_AUTOMATION_REPORT.md" -or $file.Name -eq "SECURITY_POLICY_REPORT.md") {
            continue
        }

        try {
            $content = Get-Content -Path $file.FullName -Raw -ErrorAction SilentlyContinue
            if ([string]::IsNullOrWhiteSpace($content)) { continue }

            foreach ($p in $secretPatterns) {
                if ($content -match $p.Pattern) {
                    $suspiciousFound = $true
                    $failedFile = $file.FullName
                    $failedReason = $p.Name
                    break
                }
            }
        } catch {}

        if ($suspiciousFound) { break }
    }
    if ($suspiciousFound) { break }
}

if ($suspiciousFound) {
    Write-Host "`n====================================================" -ForegroundColor Red
    Write-Host "                SECURITY SCAN FAILED                " -ForegroundColor Red
    Write-Host "====================================================" -ForegroundColor Red
    Write-Host "Suspicious Secret Detected ($failedReason):" -ForegroundColor Red
    Write-Host "File: $failedFile" -ForegroundColor Red
    exit 1
}

Write-Host "`n====================================================" -ForegroundColor Green
Write-Host "                SECURITY SCAN PASSED                " -ForegroundColor Green
Write-Host "====================================================" -ForegroundColor Green
exit 0
