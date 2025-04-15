import os
from pathlib import Path
import re
import shutil
import subprocess

def get_version_from_init() -> str:
    init_file = Path("src/altium_ibom_releaser/__init__.py")
    match = re.search(r'^__version__\s*=\s*["\']([^"\']+)["\']', init_file.read_text(), re.M)
    if not match:
        raise ValueError("Version string not found in __init__.py")
    return match.group(1)

def write_version_info(version: str, output_path: Path):
    version_tuple = tuple(map(int, version.split("."))) + (0,) * (4 - version.count(".") - 1)
    text = f"""\
VSVersionInfo(
  ffi=FixedFileInfo(
    filevers={version_tuple},
    prodvers={version_tuple},
    mask=0x3f,
    flags=0x0,
    OS=0x4,
    fileType=0x1,
    subtype=0x0,
    date=(0, 0)
  ),
  kids=[
    StringFileInfo([
      StringTable(
        '040904B0',
        [
          # StringStruct('CompanyName', ''),
          StringStruct('FileDescription', 'Altium IBOM Releaser'),
          StringStruct('FileVersion', '{version}'),
          StringStruct('InternalName', 'altium_ibom_releaser'),
          StringStruct('OriginalFilename', 'altium_ibom_releaser.exe'),
          # StringStruct('ProductName', 'Altium IBOM Releaser'),
          # StringStruct('ProductVersion', '{version}')
        ]
      )
    ]),
    VarFileInfo([VarStruct('Translation', [1033, 1200])])
  ]
)
"""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(text)
    print(f"Wrote version info to {output_path}")


def build():
    import argparse
    parser = argparse.ArgumentParser(description="Build the Windows executable.")
    parser.add_argument("--stage", action="store_true", help="Stage the executable in the Git repo.")
    args = parser.parse_args()

    version = get_version_from_init()
    version_file = Path("build/version_info.txt")
    write_version_info(version, version_file)

    print("Building Windows executable using PyInstaller...")
    subprocess.check_call([
        Path(".venv/Scripts/python"),
        "-m",
        "PyInstaller",
        "--onefile",
        "--version-file", str(version_file),
        "-n", "altium_ibom_releaser",
        "src/altium_ibom_releaser/__main__.py"
    ], shell=True)

    if args.stage:
        release_path = Path("release") / "altium_ibom_releaser.exe"
        shutil.copyfile(
            Path("dist/altium_ibom_releaser.exe"),
            release_path,
        )
        print("Copied executable to release folder.")

        env = os.environ.copy()
        if not env.get("USERPROFILE", None):
            raise ValueError("USERPROFILE environment variable not set.")
        env["HOME"] = env["USERPROFILE"]
        subprocess.check_call(["git", "add", str(release_path)], env=env)
        print("Staged executable in the Git repo.")

if __name__ == "__main__":
    build()
