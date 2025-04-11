
$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest
$PSNativeCommandUseErrorActionPreference = $true # might be true by default

# Make sure that the bin directory is in the PATH
& "$PSScriptRoot\_ensure_bin_path.ps1"

$executable_path = "$PSScriptRoot\..\release\altium_ibom_releaser.exe"
& "$PSScriptRoot\Test-LfsPlaceholder.ps1" $executable_path

$binDir = "$env:USERPROFILE\bin"
$binFilePath = "$binDir\altium_ibom_releaser.exe"

Remove-Item -Path $binDir\altium_ibom_releaser.* -ErrorAction SilentlyContinue
Write-Output "Removed old executable from $binDir"

Copy-Item -Path $executable_path -Destination $binFilePath -Force
Write-Output "Executable installed to $binFilePath"
Write-Output "You can run the program by typing 'altium_ibom_releaser' in your terminal."
