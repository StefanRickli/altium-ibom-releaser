

& "$PSScriptRoot\hint_conventional_commits.ps1"

Write-Output ""
Write-Output "The following commands are available in this project:"
Write-Output "help     This script is used to provide help and usage information for the project."
Write-Output "update   This script is used to set up a fresh virtual environment, update all dependencies to the latest version"
Write-Output "         and export them to requirements.txt, and installs the pre-commit hooks."
Write-Output "setup    This script is used to set up a virtual environment according to requirements.txt, and installs"
Write-Output "         the pre-commit hooks."
Write-Output "release  This script uses ``python-semantic-release`` to create a changelog, increment the version number, build the"
Write-Output "         executable, then commit and push the result."
Write-Output ""
Write-Output "InteractiveHtmlBom is installed in the virtual environment. Run ``generate_interactive_bom --help`` for usage information."
