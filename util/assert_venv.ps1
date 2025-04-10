
if (Test-Path -Path ".\.venv") {
    # Write-Host "Virtual environment found."
} else {
    Write-Host "No virtual environment found. Please run freeze.ps1 or install.ps1 to create one."
    exit 1
}
