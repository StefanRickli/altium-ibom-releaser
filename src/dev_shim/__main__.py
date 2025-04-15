from pathlib import Path
from subprocess import CalledProcessError, check_call
from sys import exit, argv

from dev_shim.project_path import project_path

print("DEBUG: Running altium_ibom_releaser in editable mode.")
print("DEBUG: project_path:", project_path)
print("")

python_path = Path(project_path) / ".venv/Scripts/python.exe"
if not python_path.exists():
    print(f"Python executable not found at {python_path}.")
    exit(1)

try:
    check_call([
        str(python_path),
        "-m",
        "altium_ibom_releaser",
        *argv[1:]
        ])
except CalledProcessError:
    input("Press Enter to continue...")
