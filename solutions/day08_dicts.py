"""
Day 8 — Dictionaries.

A dictionary stores labelled values: each key points to a value.
"""

student = {
    "name": "Shiva Prasad",
    "branch": "ECE",
    "marks": 85,
}

print("Name:", student["name"])
print("Branch:", student["branch"])

student["marks"] = 90          # update a value
student["year"] = 3            # add a new key
print("Updated record:", student)

print()
print("Everything in the record:")
for key, value in student.items():
    print(f"{key}: {value}")
