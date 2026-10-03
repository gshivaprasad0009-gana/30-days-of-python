"""
Day 14 — Put it together.

A small student report using loops, conditions and string formatting.
"""


def build_report(students):
    lines = ["Student Report", "=" * 20]
    total = 0
    for name, marks in students:
        status = "Pass" if marks >= 40 else "Fail"
        lines.append(f"{name:<10} {marks:>4}  {status}")
        total += marks
    average = total / len(students)
    lines.append("=" * 20)
    lines.append(f"Average: {average:.1f}")
    return "\n".join(lines)


if __name__ == "__main__":
    students = [("Shiva", 85), ("Ravi", 72), ("Anu", 91), ("Kiran", 35)]
    print(build_report(students))
