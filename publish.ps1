$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest
$PSNativeCommandUseErrorActionPreference = $true # might be true by default

.\util\assert_venv.ps1
.\.venv\Scripts\Activate.ps1

Write-Output "TBD!"
# semantic-release publish
