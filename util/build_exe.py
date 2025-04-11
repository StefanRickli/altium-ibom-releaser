from pathlib import Path
import shutil
import subprocess

def build():
    import argparse
    parser = argparse.ArgumentParser(description="Build the Windows executable.")
    parser.add_argument("--stage", action="store_true", help="Stage the executable in the Git repo.")
    args = parser.parse_args()

    print("Building Windows executable using PyInstaller...")
    subprocess.check_call([
        Path(".venv/Scripts/python"),
        "-m",
        "PyInstaller",
        "--onefile",
        "-n", "altium_ibom_releaser",
        "src/altium_ibom_releaser/__main__.py"
    ], shell=True)

    release_path = Path("release") / "altium_ibom_releaser.exe"

    shutil.copyfile(
        Path("dist/altium_ibom_releaser.exe"),
        release_path,
    )
    print("Copied executable to release folder.")

    if args.stage:
        subprocess.check_call(["git", "add", str(release_path)])
        print("Staged executable in the Git repo.")

if __name__ == "__main__":
    build()
