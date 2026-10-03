"""
Day 11 — While loops.

A while loop repeats until a condition becomes false.
"""

print("Countdown:")
n = 5
while n > 0:
    print(n)
    n -= 1
print("Lift off!")

print()
print("A guessing loop (demo run, no typing needed):")
secret = 7
tries = 0
for guess in [3, 9, 7]:
    tries += 1
    if guess == secret:
        print(f"Correct! It was {secret}, found in {tries} tries.")
        break
    print(f"{guess} is not right, trying again...")
