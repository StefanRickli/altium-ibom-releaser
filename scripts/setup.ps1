# Use this script to develop in a virtual environment that has all the dependencies of the latest
# freeze.ps1 script invocation installed. Pre-commit hooks are also installed.

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest
$PSNativeCommandUseErrorActionPreference = $true # might be true by default

Push-Location $PSScriptRoot\..
try {

    $new_virtualenv = $false
    # Remove preexisting .venv folder
    if (-Not (Test-Path .\.venv)) {
        $new_virtualenv = $true

        Write-Host "Creating new virtual environment..."
        $pythonPath = "$PSScriptRoot\Get-PythonPath.py"
        & $pythonPath -m venv .venv
    } else {
        Write-Output "Reusing existing virtual environment..."
    }

    # Activate the virtual environment
    Write-Output "Activating the virtual environment..."
    & .\.venv\Scripts\Activate.ps1

    # Install the package
    Write-Output "Installing package (with dev dependencies)..."
    pip install -r requirements.txt --no-deps -e .

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
