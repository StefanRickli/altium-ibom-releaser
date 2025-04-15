
$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest
$PSNativeCommandUseErrorActionPreference = $true # might be true by default

# Throws if python is not in PATH
$systemPythonPath = "$PSScriptRoot\Get-SystemPythonPath.py"
Write-Output "Found system python at $systemPythonPath"

# Install the virtual environment with requirements if it doesn't already exist
& "$PSScriptRoot\setup.ps1"

# Build dev shim
& "$PSScriptRoot\build_dev_shim.ps1"

# Make sure that the bin directory is in the PATH
& "$PSScriptRoot\_ensure_bin_path.ps1"
$binDir = "$env:USERPROFILE\bin"
$shimFilePath = "$PSScriptRoot\..\dist\dev_shim.exe"
$exeFilePath = "$binDir\altium_ibom_releaser.exe"

Remove-Item -Path $binDir\altium_ibom_releaser.exe -ErrorAction SilentlyContinue
Write-Output "Removed old executable from $binDir"

Copy-Item -Path $shimFilePath -Destination $exeFilePath -Force
Write-Output "Shim installed to $exeFilePath"
Write-Output "You can run the program by typing 'altium_ibom_releaser' in your terminal."
