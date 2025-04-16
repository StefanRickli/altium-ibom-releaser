import csv
from dataclasses import dataclass, field
import json
from pathlib import Path
from typing import Any
import logging

from altium_ibom_releaser.common import PatchResult, PatchStatus, Paths

moduleLogger = logging.getLogger(__name__)

tmp_dir = Path("./tmp")

@dataclass
class Field:
    name: str = ""
    slice: tuple[int, int] = (0, 0)

@dataclass
class FileInfo:
    date: str = ""
    time: str = ""
    revision: str = ""
    variant: str = ""
    units_used: str = ""
    fields: dict[str, Field] = field(default_factory=dict)
    data_offset: int = 0

def parse_header(lines: list[str], txt: bool = True) -> FileInfo:
    assert lines
    assert "Altium Designer Pick and Place Locations" in lines[0], "Invalid PNP file header."

    file_info = FileInfo()

    file_info_block_data_offset = 0
    for i, line in enumerate(lines):
        if not line.split():
            continue
        if line.startswith("Date:"):
            # Split by whitespace, save the date, remember offset of date string
            file_info.date = line.split()[1]
            file_info_block_data_offset = line.index(file_info.date)
            continue
        if line.startswith("Time:"):
            file_info.time = line[file_info_block_data_offset:]
            continue
        if line.startswith("Revision:"):
            file_info.revision = line[file_info_block_data_offset:]
            continue
        if line.startswith("Variant:"):
            file_info.variant = line[file_info_block_data_offset:]
            continue
        if line.startswith("Units used:"):
            file_info.units_used = line[file_info_block_data_offset:]
            continue
        if "Designator" in line:
            if txt:
                file_info.fields = extract_fields(line, csv)
                file_info.data_offset = i + 1  # Data starts after the header line
            else:
                file_info.fields = {}
                file_info.data_offset = i # Include header line for csv parser
            return file_info
    else:
        raise ValueError("No header line found in PNP file.")

def extract_fields(line: str, csv: bool) -> list[Field]:
    """Extract fields from the header line."""
    fields = []
    field_names = line.split()
    n_fields = len(field_names)
    for i, field_name in enumerate(field_names):
        if i > 0:
            # Add previous field slice's end index
            fields[-1].slice = (fields[-1].slice[0], line.index(field_name))
        fields.append(Field(name=field_name, slice=(line.index(field_name), -1)))
        if i == n_fields - 1:
            # Last field slice's end index
            fields[-1].slice = (fields[-1].slice[0], None)
    return {f.name: f for f in fields}

def extract_components_csv(pnp_file_contents: str) -> tuple[dict, FileInfo]:
    lines = pnp_file_contents.strip().splitlines()
    file_info = parse_header(lines, txt=False)
    reader = csv.DictReader(lines[file_info.data_offset:])
    file_info.fields = reader.fieldnames
    components = {component["Designator"]: component for component in reader}
    return (components, file_info)

def extract_components_txt(pnp_file_contents: str) -> tuple[dict, FileInfo]:
    lines = pnp_file_contents.strip().splitlines()
    file_info = parse_header(lines)
    moduleLogger.debug(file_info)
    components = {}
    for line in lines[file_info.data_offset:]:
        if line.strip() == "":
            continue
        new_component = {}
        for field in file_info.fields.values():
            start, end = field.slice
            value = cleanup_string(line[start:end])
            new_component[field.name] = value
        components[new_component["Designator"]] = new_component
    return (components, file_info)

def cleanup_string(s: str):
    """ Remove leading, trailing double quotes and spaces from string """
    s = s.strip()
    if s.startswith('"') and s.endswith('"'):
        s = s[1:-1]
    return s.strip()

def load_ibom_json(file_path: Path) -> dict:
    return json.loads(file_path.read_text(encoding="utf-8"))

def assert_no_missing_cols(config: dict[str, Any], pnp_file_info: FileInfo) -> None:
    """Check if the PNP file has all the required columns."""
    missing_cols = set(config["SelectedColumns"]) - set(pnp_file_info.fields)
    if missing_cols:
        raise ValueError(f"Configured InteractiveHTMLBOM4Altium to use columns {missing_cols}, but PNP file is missing them.")

@dataclass
class Component:
    idx: int
    attrs: dict[str, Any]

def patch_output(paths: Paths, config: dict[str, Any]) -> PatchResult:
    assert isinstance(paths, Paths), "paths must be a Paths object."
    assert paths.pnp_file.exists(), f"PNP file {paths.pnp_file} does not exist."
    assert paths.no_variation_json_file.exists(), f"JSON file {paths.no_variation_json_file} does not exist."

    result = PatchResult()

    ibom_json = load_ibom_json(paths.no_variation_json_file)
    ibom_components = reversed([Component(i, attrs) for i, attrs in enumerate(ibom_json["components"])])

    moduleLogger.debug(f"Processing PNP file: {paths.pnp_file}")
    if paths.pnp_file.suffix == ".csv":
        variant_components, pnp_file_info = extract_components_csv(paths.pnp_file.read_text(encoding="windows-1252"))
    else:
        variant_components, pnp_file_info = extract_components_txt(paths.pnp_file.read_text(encoding="windows-1252"))
    assert_no_missing_cols(config, pnp_file_info)
    visited_components = set()
    for component in ibom_components:
        if component.attrs["ref"] not in variant_components.keys():
            # del ibom_json["components"][component.idx]
            ibom_json["components"][component.idx]["extra_fields"]["dnp"] = "DNP"
            continue
        ibom_json["components"][component.idx]["footprint"] = variant_components[component.attrs["ref"]]["Footprint"]
        if "Value" in config["SelectedColumns"]:
            ibom_json["components"][component.idx]["val"] = variant_components[component.attrs["ref"]][config["ValueParameterName"]]
        for field_name in config["SelectedColumns"]:
            ibom_json["components"][component.idx]["extra_fields"][field_name] = variant_components[component.attrs["ref"]][field_name]
        visited_components.add(component.attrs["ref"])

    if has_extra_components(variant_components, visited_components):
        moduleLogger.error("Extra components found in PNP file!")
        ibom_json["pcbdata"]["metadata"]["title"] += " (❌ INCOMPLETE ❌)"
        result.status = PatchStatus.ERROR
        result.message = ("The iBOM HTML very likely has missing components.\n"
                          "The conversion only works correctly with variants if you use the Project Releaser.")

    if "font_data" in ibom_json["pcbdata"].keys():
        # Let InteractiveHtmlBom generate the font_data and use its default font
        del ibom_json["pcbdata"]["font_data"]

    ibom_json["pcbdata"]["metadata"]["date"] = pnp_file_info.date

    (paths.target_json_file.parent).mkdir(parents=True, exist_ok=True)
    paths.target_json_file.write_text(json.dumps(ibom_json, indent=4), encoding="utf-8")

    return result

def has_extra_components(variant_components: dict, visited_components: set) -> bool:
    """Check if there are extra components in the PNP file that are not in the IBOM JSON."""
    for component in variant_components.keys():
        if component not in visited_components:
            return True
    return False
