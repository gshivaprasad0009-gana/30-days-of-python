"""
Day 26 — A helper you will actually reuse.

The ESP32 project's dashboard converts Celsius to Fahrenheit. This is that
conversion, written as a small reusable pair of functions.
"""


def celsius_to_fahrenheit(celsius):
    return round(celsius * 9 / 5 + 32, 1)


def fahrenheit_to_celsius(fahrenheit):
    return round((fahrenheit - 32) * 5 / 9, 1)


if __name__ == "__main__":
    print("ESP32 reading 28.5 C =", celsius_to_fahrenheit(28.5), "F")
    print("A 100 F day =", fahrenheit_to_celsius(100), "C")
