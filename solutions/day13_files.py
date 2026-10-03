"""
Day 13 — Files.

Write text to a file, then read it back.
"""

import os


def main():
    path = "practice_notes.txt"

    with open(path, "w") as f:          # "w" = write (creates or replaces)
        f.write("Day 13: learning to write files\n")
        f.write("Python makes this easy.\n")

    with open(path) as f:               # default mode is read
        content = f.read()

    print("File contents:")
    print(content)

    os.remove(path)                     # tidy up after ourselves


if __name__ == "__main__":
    main()
