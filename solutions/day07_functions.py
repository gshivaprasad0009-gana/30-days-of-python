"""
Day 7 — Functions.

A function is a named block of code you can call whenever you need it.
"""


def greet(name):
    return f"Hello, {name}!"


def add(a, b):
    return a + b


if __name__ == "__main__":
    print(greet("Shiva"))
    print("2 + 3 =", add(2, 3))
