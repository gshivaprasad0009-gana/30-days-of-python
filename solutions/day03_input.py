"""
Day 3 — Input and output.

input() asks the user for text. A function keeps the logic testable.
"""


def greet(name):
    """Return a greeting for the given name."""
    return f"Hello, {name}! Welcome to Python."


if __name__ == "__main__":
    user_name = input("What is your name? ")
    print(greet(user_name))
