# Use this script to update all dependencies to the latest version and export them to requirements.txt.

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest
$PSNativeCommandUseErrorActionPreference = $true # might be true by default

# First, make sure that pwd is where the script is located
Set-Location $PSScriptRoot

if (Test-Path .\.venv) {
    Write-Host "Removing existing virtual environment..."
    Remove-Item .\.venv -Recurse -Force -ErrorAction SilentlyContinue
}

Write-Output "Creating a new virtual environment..."
py -m venv .venv

Write-Output "Activating the virtual environment..."
& .\.venv\Scripts\Activate.ps1

Write-Output "Installing package (with dev dependencies)..."
pip install -e .[dev]

Write-Output "Updating pre-commit hooks..."
pre-commit autoupdate

Write-Output "Installing pre-commit hooks..."
pre-commit install

Write-Output "Exporting installed packages to requirements.txt..."
Write-Output "# This file is automatically generated by freeze.ps1. Do not edit it manually." > requirements.txt
pip list --format freeze --exclude-editable >> requirements.txt
