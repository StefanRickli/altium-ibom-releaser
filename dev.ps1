# switch on first argument and call different scripts based on it
param (
    [string]$arg1
)

# Check if the argument is provided
if (-not $arg1) {
    & "$PSScriptRoot\scripts\help.ps1"
    exit 0
}

# Check if the argument is a valid command
$validCommands = @("help", "update", "setup", "build", "release")
if ($validCommands -notcontains $arg1) {
    Write-Host "Invalid argument. Valid arguments are: $($validCommands -join ', ')"
    exit 1
}

# Now, switch on the first argument and call different scripts based on it
switch ($arg1) {
    "help" {
        & "$PSScriptRoot\scripts\help.ps1"
    }
    "update" {
        & "$PSScriptRoot\scripts\update.ps1"
    }
    "setup" {
        & "$PSScriptRoot\scripts\setup.ps1"
    }
    "build" {
        & "$PSScriptRoot\scripts\build.ps1"
    }
    "release" {
        & "$PSScriptRoot\scripts\release.ps1"
    }
    default {
        Write-Host "Invalid argument. Valid arguments are: $($validCommands -join ', ')"
        exit 1
    }
}
