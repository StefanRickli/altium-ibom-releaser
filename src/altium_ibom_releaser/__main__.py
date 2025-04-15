"""Main entry point. Will be called if the module is run as a script."""

import argparse
from pathlib import Path

from altium_ibom_releaser.patch_json import process_release_directory

def main():
    parser = argparse.ArgumentParser(description="Process an Altium release directory, patching all variant's iBOM JSON.")
    parser.add_argument("release_dir", type=str, help="Path to the release directory.")
    args = parser.parse_args()

    # Call the function to process the release directory
    process_release_directory(Path(args.release_dir))

if __name__ == "__main__":
    main()
