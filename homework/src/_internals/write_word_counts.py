from pathlib import Path
from typing import Dict


def write_word_counts(counter: Dict[str, int], output_dir: str) -> Path:
    """Write the counter values as TSV inside the output directory."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    results_path = output_path / "wordcount.tsv"
    with results_path.open("w", encoding="utf-8") as f:
        for word in sorted(counter):
            f.write(f"{word}\t{counter[word]}\n")
    return results_path
