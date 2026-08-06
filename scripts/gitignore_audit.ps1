<#
.SYNOPSIS
    VNEXIFY Creator OS GitIgnore Security Audit Script

.DESCRIPTION
    Audits the project .gitignore file to verify that all mandatory secret,
    certificate, key, credential, build artifact, and editor patterns are excluded.

.EXAMPLE
    .\scripts\gitignore_audit.ps1
#>

[CmdletBinding()]
param ()

$ErrorActionPreference = "Stop"

Write-Host "====================================================" -ForegroundColor Cyan
Write-Host "     VNEXIFY Creator OS - GitIgnore Security Audit   " -ForegroundColor Cyan
Write-Host "====================================================" -ForegroundColor Cyan

if (-not (Test-Path ".gitignore")) {
    Write-Host "[FAIL] GitIgnore Audit Failed: .gitignore file not found in project root." -ForegroundColor Red
    exit 1
}

$gitignoreContent = Get-Content -Path ".gitignore"

$requiredEntries = @(
    ".env",
    ".env.*",
    "!.env.example",
    "*.pem",
    "*.key",
    "*.crt",
    "*.cer",
    "*.p12",
    "*.pfx",
    "credentials.json",
    "service-account.json",
    "firebase-adminsdk.json",
    "secret.json",
    "secrets.json",
    "token.json",
    "oauth.json",
    ".vscode/",
    ".idea/",
    "__pycache__/",
    "*.pyc",
    ".pytest_cache/",
    ".mypy_cache/",
    "npm-debug.log*",
    "yarn-error.log*",
    "pnpm-debug.log*"
)

$missingEntries = [System.Collections.Generic.List[string]]::new()

foreach ($entry in $requiredEntries) {
    $found = $false
    foreach ($line in $gitignoreContent) {
        $trimmed = $line.Trim()
        if ($trimmed -eq $entry -or $trimmed.StartsWith($entry)) {
            $found = $true
            break
        }
    }
    if (-not $found) {
        $missingEntries.Add($entry)
    }
}

if ($missingEntries.Count -gt 0) {
    Write-Host "`n====================================================" -ForegroundColor Red
    Write-Host "               GitIgnore Audit Failed               " -ForegroundColor Red
    Write-Host "====================================================" -ForegroundColor Red
    Write-Host "Missing Required Entries in .gitignore:" -ForegroundColor Red
    foreach ($missing in $missingEntries) {
        Write-Host " - $missing" -ForegroundColor Red
    }
    exit 1
}

Write-Host "`n====================================================" -ForegroundColor Green
Write-Host "               GitIgnore Audit Passed               " -ForegroundColor Green
Write-Host "====================================================" -ForegroundColor Green
exit 0
