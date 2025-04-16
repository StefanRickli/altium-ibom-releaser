"""Main entry point. Will be called if the module is run as a script."""

from dataclasses import dataclass
import logging
import os
import sys
import argparse
from pathlib import Path
import logging
from typing import Any

from altium_ibom_releaser.common import PatchStatus, Paths
from altium_ibom_releaser.util import init_logging

# Prevent InteractiveHtmlBom from trying to load not-installed packaged `pcbnew`
os.environ["INTERACTIVE_HTML_BOM_CLI_MODE"] = "1"
import InteractiveHtmlBom.generate_interactive_bom as ibom

from altium_ibom_releaser.patch_json import patch_json

moduleLogger = logging.getLogger(__name__)


def get_variant(pnp_file: Path) -> str:
    lines = pnp_file.read_text(encoding="windows-1252").splitlines()
    for line in lines:
        if line.startswith("Variant"):
            return " ".join(line.split(" ")[1:]).strip()
    else:
        raise ValueError("Variant not found in PNP file.")

def find_json_file(search_dir: Path) -> Path | None:
    if target_json_file := next(search_dir.rglob("*.json"), None):
        return target_json_file
    else:
        raise FileNotFoundError(f"JSON file not found in {search_dir}.")

def find_pnp_file(search_dir: Path) -> Path | None:
    candidates_files = search_dir.rglob("*.csv")
    for pnp_file in candidates_files:
        if any(search_term in pnp_file.name.lower() for search_term in ("pick place", "pickandplace", "pick&place", "pnp")):
            return pnp_file
    return None

def is_project_release(current_dir: Path) -> bool:
    return all(search_term in str(current_dir) for search_term in ("TempReleases", "Snapshot"))

def get_release_dir(current_dir: Path) -> Path:
    for parent in current_dir.parents:
        if (parent / "Assembly").exists():
            return parent

def get_assembly_dir(current_path: Path) -> Path:
    for parent in current_path.parents:
        if "Assembly" in parent.name:
            return parent

def find_files(start_dir: Path, extend_search: bool = True) -> Paths | None:
    json_file = find_json_file(start_dir)
    if not (cfg_file := json_file.with_suffix(".cfg")).exists():
        raise FileNotFoundError(f"CFG file not found in '{start_dir}'.")
    if not (pnp_file := find_pnp_file(start_dir)):
        if not (pnp_file := find_pnp_file(start_dir.parent)):
            raise FileNotFoundError(f"PNP file not found in '{start_dir}'.")
    target_json_file = json_file.with_stem(json_file.stem + "_patched")

    if is_project_release(start_dir):
        moduleLogger.debug("Project Release detected.")
        # Extract the folder structure that target_json_file was in, and apply it to the
        # release_dir to find the no_variant_json_file.
        release_dir = get_release_dir(start_dir)
        json_file_rel_subdir = json_file.parent.relative_to(get_assembly_dir(json_file))
        no_variant_json_dir = (release_dir / "Assembly" / json_file_rel_subdir)
        if not (no_variant_json_file := next(no_variant_json_dir.glob("*.json"))):
            raise FileNotFoundError(f"JSON file not found in '{no_variant_json_dir}'.")
    else:
        no_variant_json_file = json_file
    return Paths(pnp_file, no_variant_json_file, target_json_file, cfg_file)

def parse_config(config_raw: str) -> dict[str, Any]:
    config_lines = config_raw.split('|')
    config_dict = {}
    for line in config_lines:
        if not line.strip():
            continue
        key, value = line.split("=", 1)
        if key.strip() == "ColumnsParametersNames":
            config_dict["SelectedColumns"] = [col.strip().replace("[","").replace("]","") for col in value.split(",")]
        else:
            config_dict[key.strip()] = value.strip()
    return config_dict

def main():
    init_logging()

    parser = argparse.ArgumentParser(description="Process an Output Job directory, patching its iBOM JSON, and generating HTML.")
    parser.add_argument("outjob_dir", type=str, help="Path to the Output Job directory.")
    args = parser.parse_args()

    # Remove a trailing double quote in the path if it exists
    # This is a workaround for a bug in the Altium Designer scripting engine that adds a double quote at the end of the path.
    paths = find_files(Path(args.outjob_dir.rstrip('"')))

    config_raw = paths.cfg_file.read_text(encoding="windows-1252")
    config = parse_config(config_raw)

    patch_result = patch_json(paths, config)

    # sys.argv = ["InteractiveHtmlBom", "-h"]
    sys.argv = [
        "InteractiveHtmlBom",
        "--no-browser",
        "--dest-dir",
        ".",
        "--dnp-field",
        "dnp",
        "--show-fields",
        ",".join(config["SelectedColumns"]),
        str(paths.target_json_file),
        ]
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
