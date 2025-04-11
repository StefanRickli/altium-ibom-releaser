# switch on first argument and call different scripts based on it
param (
    [string]$arg1
)

function Show-Help {
    Write-Host "Usage: install.ps1 <command>"
    Write-Host ""
    Write-Host "Available commands:"
    Write-Host "exe:      Install the standalone, pre-built executable version."
    Write-Host "editable: Install the editable version, using a virtual environment (Python Installation required)."
}

# Check if the argument is provided
if (-not $arg1) {
    Show-Help
    exit 0
}

# Check if the argument is a valid command
$validCommands = @("help", "exe", "editable")
if ($validCommands -notcontains $arg1) {
    Write-Host "Invalid argument. Valid arguments are: $($validCommands -join ', ')"
    exit 1
}

# Now, switch on the first argument and call different scripts based on it
switch ($arg1) {
    "help" {
        Show-Help
        exit 0
    }
    "exe" {
        & "$PSScriptRoot\scripts\install_exe.ps1"
        exit 0
    }
    "editable" {
        & "$PSScriptRoot\scripts\install_editable.ps1"
        exit 0
    }
    default {
        Write-Host "Invalid argument. Valid arguments are: $($validCommands -join ', ')"
        exit 1
    }
}
