"""
Day 19 — Word counter.

Count how many times each word appears in some text.
"""


def count_words(text):
    """Return a dictionary of word -> count."""
    counts = {}
    for word in text.split():
        word = word.lower().strip(".,!?")
        counts[word] = counts.get(word, 0) + 1
    return counts


if __name__ == "__main__":
    sample = "the quick brown fox jumps over the lazy dog the end"
    counts = count_words(sample)
    for word, number in counts.items():
        print(f"{word}: {number}")
