"""
Day 16 — Number guessing game.

The program picks a number; the player guesses. "Too low" / "too high" guides them.
"""

import random


def play(secret, guesses):
    """Play with a list of guesses and report the outcome."""
    for number, guess in enumerate(guesses, start=1):
        if guess == secret:
            return f"Correct! It was {secret}. You took {number} guesses."
        if guess < secret:
            print(f"{guess} is too low")
        else:
            print(f"{guess} is too high")
    return f"Out of guesses. It was {secret}."


if __name__ == "__main__":
    secret = random.randint(1, 10)
    print("Guess a number between 1 and 10 (demo run)")
    print(play(secret, [5, 8, 2, 9, 7]))
