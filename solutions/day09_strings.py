"""
Day 9 — Strings.

Text is a string. You can loop over its characters.
"""


def count_vowels(word):
    """Count how many vowels are in a word."""
    vowels = "aeiou"
    count = 0
    for letter in word.lower():     # .lower() so 'A' counts as 'a'
        if letter in vowels:
            count += 1
    return count


if __name__ == "__main__":
    word = input("Enter a word: ")
    print(f"{word} has {count_vowels(word)} vowels.")
