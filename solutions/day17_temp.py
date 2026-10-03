"""
Day 17 — Temperature converter.

Celsius to Fahrenheit and back. The same maths the ESP32 dashboard uses.
"""


def c_to_f(celsius):
    return celsius * 9 / 5 + 32


def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


if __name__ == "__main__":
    print("25 C =", round(c_to_f(25), 1), "F")
    print("77 F =", round(f_to_c(77), 1), "C")
