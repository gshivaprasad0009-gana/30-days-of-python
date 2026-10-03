"""
Day 21 — Refactor.

Take the things you wrote earlier and rewrite them as small, clear functions.
Good code is code you can read again next month.
"""


def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def average(numbers):
    return sum(numbers) / len(numbers)


def grade(mark):
    if mark >= 90:
        return "A"
    if mark >= 75:
        return "B"
    if mark >= 40:
        return "C"
    return "F"


if __name__ == "__main__":
    print("Temperatures:", [celsius_to_fahrenheit(c) for c in [0, 25, 100]])
    marks = [85, 72, 91]
    print("Average mark:", average(marks))
    print("Grades:", [grade(m) for m in marks])
