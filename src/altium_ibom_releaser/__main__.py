"""Main entry point. Will be called if the module is run as a script."""

import logging
import os
import sys
import argparse
from pathlib import Path

# Prevent InteractiveHtmlBom from trying to load not-installed packaged `pcbnew`
os.environ["INTERACTIVE_HTML_BOM_CLI_MODE"] = "1"
import InteractiveHtmlBom.generate_interactive_bom as ibom

from altium_ibom_releaser.patch_json import process_release_directory

def main():
    parser = argparse.ArgumentParser(description="Process an Altium release directory, patching all variant's iBOM JSON.")
    parser.add_argument("release_dir", type=str, help="Path to the release directory.")
    args = parser.parse_args()

    # Call the function to process the release directory
    processed_dirs = process_release_directory(Path(args.release_dir))

    for variant_dir, json_file in processed_dirs:
        print(f"Processed variant directory: {variant_dir}")
        # original_argv = sys.argv
        sys.argv = ["InteractiveHtmlBom", "--no-browser", "--dest-dir", ".", str(json_file)]
        logger = logging.getLogger('InteractiveHtmlBom')
        logger.handlers.clear()
        ibom.main()


if __name__ == "__main__":
    main()
