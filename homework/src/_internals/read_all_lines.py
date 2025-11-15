from pathlib import Path
from typing import List


def read_all_lines(input_dir: str) -> List[str]:
    """Read every line from plain-text files inside input_dir."""
    base_path = Path(input_dir)
    if not base_path.exists():
        raise FileNotFoundError(f"Input directory '{input_dir}' does not exist")

    all_lines: List[str] = []
    for path in sorted(base_path.iterdir()):
        if path.is_file():
            with path.open("r", encoding="utf-8") as f:
                all_lines.extend(f.readlines())
    return all_lines
