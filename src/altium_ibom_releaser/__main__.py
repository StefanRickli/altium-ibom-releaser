"""Main entry point. Will be called if the module is run as a script."""

from dataclasses import dataclass
import logging
import os
import sys
import argparse
from pathlib import Path
import logging
from colorlog import ColoredFormatter

from altium_ibom_releaser.common import PatchStatus, Paths
from altium_ibom_releaser.util import init_logging

# Prevent InteractiveHtmlBom from trying to load not-installed packaged `pcbnew`
os.environ["INTERACTIVE_HTML_BOM_CLI_MODE"] = "1"
import InteractiveHtmlBom.generate_interactive_bom as ibom

from altium_ibom_releaser.patch_json import patch_output

moduleLogger = logging.getLogger(__name__)


def get_variant(pnp_file: Path) -> str:
    lines = pnp_file.read_text(encoding="windows-1252").splitlines()
    for line in lines:
        if line.startswith("Variant"):
            return " ".join(line.split(" ")[1:]).strip()
    else:
        raise ValueError("Variant not found in PNP file.")

def is_project_release(script_dir: Path) -> bool:
    # base_dir might be the following path:
    # C:\Users\srickli\AppData\Local\TempReleases\Snapshot\1\Assembly VariantName
    # We look for a sibling folder of "Assembly VariantName" named "Assembly"
    if next(script_dir.parent.glob("Assembly"), None):
        return True
    return False

def find_files(variant_dir: Path, extend_search: bool = True) -> Paths | None:
    pnp_file = next((variant_dir / "Pick Place").glob("*.csv"), None)
    if not pnp_file:
        if extend_search:
            if paths := find_files(variant_dir.parent, extend_search=False):
                return paths
            elif paths := find_files(variant_dir / "Script", extend_search=False):
                return paths
            else:
                raise FileNotFoundError(f"PNP file not found in '{variant_dir}'.")
        else:
            return None
    if is_project_release(variant_dir):
        moduleLogger.debug("Project Release detected.")
        release_dir = variant_dir.parent
        no_variant_json_file = next((release_dir / "Assembly/Script").glob("*.json"), None)
        if not no_variant_json_file:
            raise FileNotFoundError(f"JSON file not found in '{release_dir / 'Assembly/Script'}'.")
        target_json_file = (variant_dir / f"Script/{pnp_file.stem.replace("Pick Place", "iBOM")}_patched.json")
    else:
        moduleLogger.debug("Not in a Project Release.")
        if get_variant(pnp_file) != "No Variation":
            moduleLogger.warning("Direct OutJob invocation with a variant! JSON might be incomplete!")
        no_variant_json_file = next((variant_dir / "Script").glob("*.json"), None)
        target_json_file = no_variant_json_file.with_stem(pnp_file.stem.replace("Pick Place", "iBOM") + "_patched")
    return Paths(pnp_file, no_variant_json_file, target_json_file)

def main():
    init_logging()

    parser = argparse.ArgumentParser(description="Process an Output Job directory, patching its iBOM JSON, and generating HTML.")
    parser.add_argument("outjob_dir", type=str, help="Path to the Output Job directory.")
    args = parser.parse_args()

    paths = find_files(Path(args.outjob_dir))
    if paths.pnp_file.parent != paths.no_variation_json_file.parent:
        patch_result = patch_output(paths)

    sys.argv = ["InteractiveHtmlBom", "--no-browser", "--dest-dir", ".", str(paths.target_json_file)]
    logger = logging.getLogger('InteractiveHtmlBom')
    logger.handlers.clear()
    ibom.main()

    if patch_result.status == PatchStatus.WARNING:
        moduleLogger.warning(patch_result.message)
    elif patch_result.status == PatchStatus.ERROR:
        moduleLogger.error(patch_result.message)
        sys.exit(1)

if __name__ == "__main__":
    main()
