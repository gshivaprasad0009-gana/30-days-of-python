"""
Day 4 — If / else.

Conditions let the program choose between paths.
"""


def result(mark):
    """Turn a mark into a short description."""
    if mark >= 90:
        return "Excellent"
    elif mark >= 75:
        return "Very good"
    elif mark >= 40:
        return "Pass"
    else:
        return "Fail"


if __name__ == "__main__":
    mark = float(input("Enter your mark: "))
    print(result(mark))
