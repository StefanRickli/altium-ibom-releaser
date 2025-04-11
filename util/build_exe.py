from pathlib import Path
import subprocess

def build():
    print("Building Windows executable using PyInstaller...")
    subprocess.check_call([
        Path(".venv/Scripts/python"),
        "-m",
        "PyInstaller",
        "--onefile",
        "-n", "altium_ibom_releaser",
        "src/altium_ibom_releaser/__main__.py"
    ], shell=True)
    print("Wrote executable to dist/altium_ibom_releaser.exe")

if __name__ == "__main__":
    build()
