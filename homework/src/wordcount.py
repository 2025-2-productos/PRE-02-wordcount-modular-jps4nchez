from ._internals.count_words import count_words
from ._internals.preprocess_lines import preprocess_lines
from ._internals.read_all_lines import read_all_lines
from ._internals.split_into_words import split_into_words
from ._internals.write_word_counts import write_word_counts


def main(input_dir: str = "data/input", output_dir: str = "data/output"):
    """Full pipeline: read, preprocess, split, count, and persist results."""
    all_lines = read_all_lines(input_dir)
    normalized_lines = preprocess_lines(all_lines)
    words = split_into_words(normalized_lines)
    counter = count_words(words)
    write_word_counts(counter, output_dir)
    return counter


if __name__ == "__main__":
    main()
