"""
Day 20 — Quiz program.

Ask questions, check the answers, report a score.
"""

questions = [
    ("What is the unit of resistance?", "ohm"),
    ("What does LED stand for?", "light emitting diode"),
    ("What is 5 x 6?", "30"),
]


def score(answers):
    """Return how many answers were correct."""
    correct = 0
    for (question, expected), given in zip(questions, answers):
        if given.lower().strip() == expected:
            correct += 1
    return correct


if __name__ == "__main__":
    print("Quiz demo")
    answers = ["ohm", "light emitting diode", "31"]
    print(f"Score: {score(answers)} / {len(questions)}")
