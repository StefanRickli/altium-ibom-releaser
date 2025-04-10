# First, make sure that pwd is where the script is located
Set-Location $PSScriptRoot

# Remove preexisting .venv folder
Remove-Item .\.venv -Recurse -Force -ErrorAction SilentlyContinue

# Create a new virtual environment in the .venv folder
py -m venv .venv

# Activate the virtual environment
& .\.venv\Scripts\Activate.ps1

# Install the package
pip install -e .

# Export the installed packages to requirements.txt
pip freeze > requirements.txt
