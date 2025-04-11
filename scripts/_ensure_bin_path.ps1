# This script ensures that the user's bin directory exists and is included in the PATH environment variable.

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest
$PSNativeCommandUseErrorActionPreference = $true # might be true by default


$binPath = "$env:USERPROFILE\bin"

# Create the bin directory if it doesn't exist
if (-not (Test-Path -Path $binPath)) {
    New-Item -ItemType Directory -Path $binPath | Out-Null
}

# Get the current user's PATH
$currentPath = [Environment]::GetEnvironmentVariable("PATH", "User")

# Check if binPath is already in PATH (case-insensitive)
$pathEntries = $currentPath -split ';'
$alreadyPresent = $pathEntries -contains $binPath

# If not present, add it
if (-not $alreadyPresent) {
    $newPath = "$currentPath;$binPath"
    [Environment]::SetEnvironmentVariable("PATH", $newPath, "User")
    $env:PATH += ";$binPath"  # Immediate effect in current shell
    Write-Output "Added '$binPath' to PATH."
} else {
    Write-Output "'$binPath' is already in PATH."
}
