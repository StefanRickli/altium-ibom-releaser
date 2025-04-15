# Use this script to
# 1a. Create a new virtual environment if it does not exist.
# 1b. Use a preexisting virtual environment
# 2. Install all the dependencies of requirements.txt
# 3. Install the package in editable mode with dev dependencies.
# 4. Install pre-commit hooks.

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest
$PSNativeCommandUseErrorActionPreference = $true # might be true by default

Push-Location $PSScriptRoot\..
try {
    $new_virtualenv = $false
    if (-Not (Test-Path .\.venv)) {
        $new_virtualenv = $true

        Write-Host "Creating new virtual environment..."
        $systemPythonPath = & "$PSScriptRoot\Get-SystemPythonPath.ps1"
        & $systemPythonPath -m venv .venv
    } else {
        Write-Output "Reusing existing virtual environment..."
    }

    # Activate the virtual environment
    Write-Output "Activating the virtual environment..."
    & .\.venv\Scripts\Activate.ps1

    # Install the package
    Write-Output "Installing package (with dev dependencies)..."
    & .\.venv\Scripts\python -m pip install -r requirements.txt --no-deps -e .

    # Install pre-commit hooks
    Write-Output "Activating pre-commit hooks..."
    pre-commit install

    if ($new_virtualenv) {
        # Give the user a hint about conventional commits
        Write-Output ""
        .\scripts\hint_conventional_commits.ps1
    }
} finally {
    Pop-Location
}
