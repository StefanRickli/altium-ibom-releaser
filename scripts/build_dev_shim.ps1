
$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest
$PSNativeCommandUseErrorActionPreference = $true # might be true by default

Push-Location $PSScriptRoot\..
try {

    "# File automatically created by `build_dev_shim.ps1` script. Do not edit manually." | Out-File -FilePath src/dev_shim/project_path.py -Encoding utf8
    "project_path = r'$(Resolve-Path $PSScriptRoot/..)'" | Out-File -FilePath src/dev_shim/project_path.py -Encoding utf8 -Append

    .venv/Scripts/python.exe -m PyInstaller --onefile -n dev_shim src/dev_shim/__main__.py

} finally {
    Pop-Location
}
