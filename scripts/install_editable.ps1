
$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest
$PSNativeCommandUseErrorActionPreference = $true # might be true by default

# Throws if python is not in PATH
$systemPythonPath = "$PSScriptRoot\Get-SystemPythonPath.py"
Write-Output "Found system python at $systemPythonPath"

# Install the virtual environment with requirements if it doesn't already exist
& "$PSScriptRoot\setup.ps1"

# Make sure that the bin directory is in the PATH
& "$PSScriptRoot\_ensure_bin_path.ps1"
$binDir = "$env:USERPROFILE\bin"
$templatePath = "$PSScriptRoot\shim_template.bat"
$batFilePath = "$binDir\altium_ibom_releaser.bat"

Remove-Item -Path $binDir\altium_ibom_releaser.* -ErrorAction SilentlyContinue
Write-Output "Removed old executable from $binDir"

$projectRoot = (Resolve-Path "$PSScriptRoot\..").Path
(Get-Content $templatePath) -replace 'ROOT_PLACEHOLDER', $projectRoot | Set-Content -Encoding ASCII -Path $batFilePath
Write-Output "Shim installed to $batFilePath"
Write-Output "You can run the program by typing 'altium_ibom_releaser' in your terminal."
