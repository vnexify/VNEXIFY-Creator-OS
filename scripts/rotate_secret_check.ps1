<#
.SYNOPSIS
    VNEXIFY Creator OS Secret Rotation Protocol Script

.DESCRIPTION
    Provides immediate emergency instructions and verification procedures when an
    accidental credential exposure or potential API key compromise occurs.

.EXAMPLE
    .\scripts\rotate_secret_check.ps1
    .\scripts\rotate_secret_check.ps1 -SecretType "OpenAI API Key"
#>

[CmdletBinding()]
param (
    [string]$SecretType = "API Secret / Credential"
)

Write-Host "====================================================" -ForegroundColor Red
Write-Host "     CRITICAL SECRET EXPOSURE REMEDIATION PROTOCOL   " -ForegroundColor Red
Write-Host "====================================================" -ForegroundColor Red

Write-Host "`nTarget Secret Type: $SecretType" -ForegroundColor Yellow
Write-Host "`nImmediate Action Required:" -ForegroundColor Red
Write-Host " 1. Rotate immediately." -ForegroundColor Red
Write-Host " 2. Revoke exposed credential in provider dashboard." -ForegroundColor Red
Write-Host " 3. Generate new credential." -ForegroundColor Red
Write-Host " 4. Update local .env file." -ForegroundColor Yellow
Write-Host " 5. Never commit credentials to Git." -ForegroundColor Yellow

Write-Host "`nProvider Dashboard Links for Rapid Revocation:" -ForegroundColor Cyan
Write-Host " - OpenAI:      https://platform.openai.com/api-keys" -ForegroundColor Gray
Write-Host " - Google AI:   https://aistudio.google.com/app/apikey" -ForegroundColor Gray
Write-Host " - Anthropic:   https://console.anthropic.com/settings/keys" -ForegroundColor Gray
Write-Host " - GitHub:      https://github.com/settings/tokens" -ForegroundColor Gray
Write-Host " - AWS:         https://console.aws.amazon.com/iam/" -ForegroundColor Gray

Write-Host "`n====================================================" -ForegroundColor Red
Write-Host "     Secret Rotation Verification Complete          " -ForegroundColor Red
Write-Host "====================================================" -ForegroundColor Red
exit 0
