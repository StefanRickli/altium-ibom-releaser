from pathlib import Path
import shutil
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

    shutil.copyfile(
        Path("dist/altium_ibom_releaser.exe"),
        Path("release/altium_ibom_releaser.exe"),
    )
    print("Copied executable to release folder.")

if __name__ == "__main__":
    build()
