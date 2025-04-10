.\util\hint_conventional_commits.ps1

Write-Output ""
Write-Output "The following scripts are available in this project:"
Write-Output "help.ps1         This script is used to provide help and usage information for the project."
Write-Output "freeze.ps1       This script is used to set up a virtual environment, update all dependencies to the latest version"
Write-Output "                 and export them to requirements.txt, and installs the pre-commit hooks."
Write-Output "install.ps1      This script is used to set up a virtual environment according to requirements.txt, and installs"
Write-Output "                 the pre-commit hooks."
Write-Output "new_version.ps1  This script uses ``python-semantic-release`` to create a changelog and increment the version number."
Write-Output ""
Write-Output "InteractiveHtmlBom is installed in the virtual environment. Run ``generate_interactive_bom --help`` for usage information."
