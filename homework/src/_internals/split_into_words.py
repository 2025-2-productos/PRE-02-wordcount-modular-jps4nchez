from typing import Iterable, List


def split_into_words(lines: Iterable[str]) -> List[str]:
    """Split normalized lines into words removing simple punctuation."""
    words: List[str] = []
    for line in lines:
        for word in line.split():
            token = word.strip(",.!?;:\"'()[]{}")
            if token:
                words.append(token)
    return words
