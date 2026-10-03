"""
Day 6 — Lists.

A list holds several values in order. You can add, remove and read them.
"""

subjects = ["Maths", "Physics", "Electronics", "Python"]
print("Subjects:", subjects)

subjects.append("Signals")          # add to the end
print("After adding:", subjects)

subjects.remove("Physics")          # remove by value
print("After removing Physics:", subjects)

print("First subject:", subjects[0])   # counting starts at 0
print("Total subjects:", len(subjects))
