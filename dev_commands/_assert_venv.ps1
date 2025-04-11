
if (Test-Path -Path "$PSScriptRoot\..\.venv") {
    # Write-Output "Virtual environment found."
} else {
    Write-Output "No virtual environment found. Please run freeze.ps1 or install.ps1 to create one."
    throw "Virtual environment check failed."
}
