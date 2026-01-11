# PowerShell Script to Serve MkDocs locally
$ErrorActionPreference = "Stop"

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "   EvisHome Local Documentation Server    " -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Binding to: http://localhost:8000" -ForegroundColor Green
Write-Host "(Alternative: http://evishome.local:8000 if configured in hosts)" -ForegroundColor Gray
Write-Host ""
Write-Host "Press Ctrl+C to stop."
Write-Host ""

# Ensure we are in the correct directory (where mkdocs.yml lives)
Set-Location $PSScriptRoot

# Run mkdocs serve using python module to avoid PATH issues
python -m mkdocs serve --dev-addr=0.0.0.0:8000
