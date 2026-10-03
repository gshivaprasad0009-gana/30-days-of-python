"""
Day 10 — Loops and lists together.

Build a neat table by looping over a list of records.
"""

students = [("Shiva", 85), ("Ravi", 72), ("Anu", 91)]

print(f"{'Name':<10}{'Marks':>6}")
print("-" * 16)
for name, marks in students:
    print(f"{name:<10}{marks:>6}")
