
if (Test-Path -Path "$PSScriptRoot\..\.venv") {
    # Write-Output "Virtual environment found."
} else {
    Write-Output "No virtual environment found. Please refer to ``dev.ps1 help`` for information how to create one comfortably."
    throw "Virtual environment check failed."
}
