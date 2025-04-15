from pathlib import Path
from subprocess import call
from sys import exit, argv

from dev_shim.project_path import project_path

print("DEBUG: Running altium_ibom_releaser in editable mode.")
print("DEBUG: project_path:", project_path)

python_path = Path(project_path) / ".venv/Scripts/python.exe"
if not python_path.exists():
    print(f"Python executable not found at {python_path}.")
    exit(1)

call(f"{python_path!s} -m altium_ibom_releaser " + " ".join(argv[1:]), shell=True)
