import os


def write_word_counts(
    counter: dict[str, int],
    output_dir: str = "data/output",
    filename: str = "results.tsv",
) -> str:
    """Write counts used by the migration test."""
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, filename)
    with open(output_path, "w", encoding="utf-8") as file:
        for key in sorted(counter.keys()):
            file.write(f"{key}\t{counter[key]}\n")
    return output_path
