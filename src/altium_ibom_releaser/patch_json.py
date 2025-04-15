from dataclasses import dataclass, field
import json
from pathlib import Path
from typing import Any

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

def parse_header(lines: list[str]) -> FileInfo:
    assert lines
    assert "Altium Designer Pick and Place Locations" in lines[0], "Invalid PNP file header."

    file_info = FileInfo()

    file_info_block_data_offset = 0
    for i, line in enumerate(lines):
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
        if line.startswith("Designator"):
            file_info.fields = extract_fields(line)
            file_info.data_offset = i + 1  # Data starts after the header line
            return file_info
    else:
        raise ValueError("No header line found in PNP file.")

def extract_fields(line: str) -> list[Field]:
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

def extract_components(pnp_file_contents: str) -> dict:
    lines = pnp_file_contents.strip().splitlines()
    file_info = parse_header(lines)
    print(file_info)
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
    return components

def cleanup_string(s: str):
    """ Remove leading, trailing double quotes and spaces from string """
    s = s.strip()
    if s.startswith('"') and s.endswith('"'):
        s = s[1:-1]
    return s.strip()

def load_ibom_json(file_path: Path) -> dict:
    return json.loads(file_path.read_text(encoding="utf-8"))

@dataclass
class Component:
    idx: int
    attrs: dict[str, Any]

def process_release_directory(release_dir: Path) -> list[tuple[Path, Path]]:
    assert isinstance(release_dir, Path), "release_dir must be a Path object."
    assert release_dir.exists(), f"Release directory {release_dir} does not exist."

    base_variant_dir = release_dir / "Assembly"
    variant_names = [d.name for d in release_dir.glob("*/") if d.is_dir() and d != base_variant_dir]
    print("Variants found:")
    print(variant_names)

    processed_paths = []
    for variant in variant_names:
        ibom_json = load_ibom_json((base_variant_dir / "Script").glob("*.json").__next__())
        ibom_components = reversed([Component(i, attrs) for i, attrs in enumerate(ibom_json["components"])])

        variant_dir = release_dir / variant
        pnp_file_path = (variant_dir / "Pick Place").glob("*.txt").__next__()
        if pnp_file_path.exists():
            print(f"Processing PNP file: {pnp_file_path}")
            variant_components = extract_components(pnp_file_path.read_text(encoding="utf-8"))
            for component in ibom_components:
                if component.attrs["ref"] not in variant_components.keys():
                    # del ibom_json["components"][component.idx]
                    ibom_json["components"][component.idx]["extra_fields"]["dnp"] = "DNP"
                    ibom_json["components"][component.idx]["attr"] = ""  # can be "Virtual"
                    ibom_json["components"][component.idx]["footprint"] = ""
                    # ibom_json["components"][component.idx]["layer"] = ""  # one of {"F", "B"}
                    ibom_json["components"][component.idx]["val"] = ""
                    continue
                ibom_json["components"][component.idx]["footprint"] = variant_components[component.attrs["ref"]]["Footprint"]
                ibom_json["components"][component.idx]["val"] = variant_components[component.attrs["ref"]]["Description"]
                ibom_json["components"][component.idx]["extra_fields"]["Comment"] = variant_components[component.attrs["ref"]]["Comment"]
            (tmp_dir / variant).mkdir(parents=True, exist_ok=True)
            output_file = (tmp_dir / variant / "patched_bom.json")
            output_file.write_text(json.dumps(ibom_json, indent=4), encoding="utf-8")
            processed_paths.append((variant_dir, output_file))
        else:
            print(f"PNP file not found for variant {variant}.")
    return processed_paths

if __name__ == "__main__":
    process_release_directory(Path("./tests/data/release_prepare"))
