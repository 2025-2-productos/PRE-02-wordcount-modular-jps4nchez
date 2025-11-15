from typing import Iterable, List


def preprocess_lines(lines: Iterable[str]) -> List[str]:
    """Normalize whitespace and lowercase each line."""
    return [line.strip().lower() for line in lines if line.strip()]
