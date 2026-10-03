# Reference solutions

**Read this before opening any file in this folder.**

These are **reference answers** for the daily tasks — the same way a textbook
gives you answers at the back. They are here to check your work, not to replace
it.

## How to use them properly

1. **Attempt the day yourself first.** Watch the class, write your own version
   in `practice/`, and get it running. That struggle is where the learning is.
2. **Then open the reference** and compare. Ask yourself:
   - Did mine work? Great — now, is the reference clearer?
   - Where did mine go wrong, and *why*?
   - Did the reference use something I have not seen yet?
3. **Then commit your own version**, not the reference. If you copied the
   reference, you learned nothing and the next day will be harder.

## What is in here

| File | Day | Covers |
|---|---|---|
| `day02_variables.py` | 2 | variables, types |
| `day03_input.py` | 3 | input, output, functions |
| `day04_ifelse.py` | 4 | if / elif / else |
| `day05_loops.py` | 5 | for loops, `range` |
| `day06_lists.py` | 6 | lists, append, remove |
| `day07_functions.py` | 7 | defining and calling functions |
| `day08_dicts.py` | 8 | dictionaries |
| `day09_strings.py` | 9 | strings, looping over characters |
| `day10_table.py` | 10 | loops + lists + formatting |
| `day11_while.py` | 11 | while loops, `break` |
| `day12_errors.py` | 12 | try / except |
| `day13_files.py` | 13 | reading and writing files |
| `day14_report.py` | 14 | putting it together |
| `day15_calculator.py` | 15 | branching on an operator |
| `day16_guess.py` | 16 | `random`, loops, comparisons |
| `day17_temp.py` | 17 | temperature conversion |
| `day18_todo.py` | 18 | list operations |
| `day19_wordcount.py` | 19 | dictionaries for counting |
| `day20_quiz.py` | 20 | data + scoring |
| `day21_refactor.py` | 21 | cleaning code into functions |
| `day26_helper.py` | 26 | a reusable helper pair |

Days 22–25 and 27–30 are reading, running and writing tasks rather than coding
tasks, so they have no reference file.

## A note on style

Every file here puts the logic in a **function** and calls it from a
`if __name__ == "__main__":` block. That is a habit worth copying: it makes
code testable and readable, and it is what professional Python looks like.

Run any of them with:

```bash
python solutions/day05_loops.py
```
