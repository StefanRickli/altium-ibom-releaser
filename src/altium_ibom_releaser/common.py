from dataclasses import dataclass
from enum import Enum, auto
from pathlib import Path


@dataclass
class Paths:
    pnp_file: Path
    no_variation_json_file: Path
    target_json_file: Path

class PatchStatus(Enum):
    OK = auto()
    WARNING = auto()
    ERROR = auto()

@dataclass
class PatchResult:
    status: PatchStatus = PatchStatus.OK
    message: str = ""
