# PowerShell Script to Serve MkDocs locally
$ErrorActionPreference = "Stop"

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "   EvisHome Local Documentation Server    " -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Binding to: http://evishome.local:8000" -ForegroundColor Green
Write-Host "(Ensure 127.0.0.1 evishome.local is in your hosts file)" -ForegroundColor Gray
Write-Host ""
Write-Host "Press Ctrl+C to stop."
Write-Host ""

# Ensure we are in the correct directory (where mkdocs.yml lives)
Set-Location $PSScriptRoot

# Run mkdocs serve using python module to avoid PATH issues
python -m mkdocs serve --dev-addr=0.0.0.0:8000
