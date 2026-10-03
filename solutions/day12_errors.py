"""
Day 12 — Error handling.

try / except stops the program crashing when something goes wrong.
"""


def to_number(text):
    """Return text as a number, or None if it is not a number."""
    try:
        return float(text)
    except ValueError:
        return None


if __name__ == "__main__":
    for value in ["25", "abc", "3.5"]:
        result = to_number(value)
        if result is None:
            print(f"'{value}' is not a number")
        else:
            print(f"'{value}' -> {result}")
