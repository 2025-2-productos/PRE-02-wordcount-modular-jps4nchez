from typing import Dict, Iterable


def count_words(words: Iterable[str]) -> Dict[str, int]:
    """Return a frequency dictionary for the given iterable of words."""
    counter: Dict[str, int] = {}
    for word in words:
        counter[word] = counter.get(word, 0) + 1
    return counter
