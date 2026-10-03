"""
Day 18 — To-do list.

Keep tasks in a list. This is the idea behind every task app you have used.
"""


def add_task(tasks, task):
    tasks.append(task)


def remove_task(tasks, task):
    """Remove a task. Return True if it was there."""
    if task in tasks:
        tasks.remove(task)
        return True
    return False


if __name__ == "__main__":
    tasks = []
    add_task(tasks, "Finish day 18")
    add_task(tasks, "Revise loops")
    print("To-do:", tasks)

    remove_task(tasks, "Revise loops")
    print("After finishing one:", tasks)
