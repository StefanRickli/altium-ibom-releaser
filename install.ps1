# switch on first argument and call different scripts based on it
param (
    [string]$arg1
)

# Check if the argument is provided
if (-not $arg1) {
    Write-Output "Usage: install.ps1 <command>"
    Write-Output "Available commands: exe, editable"
    exit 0
}

# Check if the argument is a valid command
$validCommands = @("exe", "editable")
if ($validCommands -notcontains $arg1) {
    Write-Host "Invalid argument. Valid arguments are: $($validCommands -join ', ')"
    exit 1
}

# Now, switch on the first argument and call different scripts based on it
switch ($arg1) {
    "exe" {
        & "$PSScriptRoot\scripts\install_exe.ps1"
    }
    "editable" {
        & "$PSScriptRoot\scripts\install_editable.ps1"
    }
    default {
        Write-Host "Invalid argument. Valid arguments are: $($validCommands -join ', ')"
        exit 1
    }
}
