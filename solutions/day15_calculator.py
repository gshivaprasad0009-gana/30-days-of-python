"""
Day 15 — Calculator.

Take two numbers and an operator, and return the result.
"""


def calculate(a, op, b):
    """Apply the operator to the two numbers, or return None if impossible."""
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            return None          # dividing by zero is not allowed
        return a / b
    return None                  # unknown operator


if __name__ == "__main__":
    a = float(input("First number: "))
    op = input("Operator (+ - * /): ")
    b = float(input("Second number: "))

    result = calculate(a, op, b)
    if result is None:
        print("That calculation is not possible")
    else:
        print(f"{a} {op} {b} = {result}")
