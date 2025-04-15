$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest
$PSNativeCommandUseErrorActionPreference = $true # might be true by default

Push-Location $PSScriptRoot\..
try {

    .\scripts\_assert_venv.ps1
    .\.venv\Scripts\Activate.ps1
    python .\scripts\build_exe.py

} finally {
    Pop-Location
}
