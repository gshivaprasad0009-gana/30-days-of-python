# 🐍 30 Days of Python

A 30-day challenge to learn Python by writing a little code every day and
committing it here. One day, one commit, one small step forward.

**Start date:** _fill this in_
**Goal:** 30 consecutive days of real practice — not 30 green squares.

---

## Why this repo exists

A GitHub contribution graph means nothing on its own. What it *represents* —
that you show up and build — is what people notice. So the rule for this repo
is simple:

> **Every commit is something I actually did.** A script I wrote, a bug I
> fixed, notes I took after reading real code. No empty commits, no
> copy-paste-for-the-sake-of-it.

Anyone can fake a green graph. Nobody can fake being able to explain their code.

---

## How to use this repo

Each day has two parts:

1. **A small program** in `practice/` — e.g. `practice/day03_input.py`
2. **A short note** in `days/` — e.g. `days/day03.md`, following the template in
   `days/_TEMPLATE.md`: what you did, what confused you, what you learned

`days/day01.md` and `practice/day01_hello.py` are a worked example — copy that
pattern.

---

## The 30-day plan

### Week 1 — Foundations

| Day | Task | File |
|---|---|---|
| 1 | Print "Hello, world" and run your first script | `practice/day01_hello.py` |
| 2 | Variables and types: store your name, age and marks, print them | `practice/day02_variables.py` |
| 3 | Input and output: ask for a name, greet the person | `practice/day03_input.py` |
| 4 | If / else: print Pass or Fail for a given mark | `practice/day04_ifelse.py` |
| 5 | Loops: print 1–10, then the 5 times table | `practice/day05_loops.py` |
| 6 | Lists: keep a list of subjects; add, remove and print them | `practice/day06_lists.py` |
| 7 | Functions: write `greet(name)` and `add(a, b)` | `practice/day07_functions.py` |

### Week 2 — Working with data

| Day | Task | File |
|---|---|---|
| 8 | Dictionaries: a small student record (name, branch, marks) | `practice/day08_dicts.py` |
| 9 | Strings: count the vowels in a word | `practice/day09_strings.py` |
| 10 | Combine loops and lists: print a marks table | `practice/day10_table.py` |
| 11 | While loops: a countdown and a guessing loop | `practice/day11_while.py` |
| 12 | Error handling: don't crash on bad input (`try`/`except`) | `practice/day12_errors.py` |
| 13 | Files: write to a text file, then read it back | `practice/day13_files.py` |
| 14 | Put it together: a small student report script | `practice/day14_report.py` |

### Week 3 — Small real programs

| Day | Task | File |
|---|---|---|
| 15 | Calculator (add, subtract, multiply, divide) | `practice/day15_calculator.py` |
| 16 | Number guessing game | `practice/day16_guess.py` |
| 17 | Temperature converter (Celsius ↔ Fahrenheit) | `practice/day17_temp.py` |
| 18 | To-do list (in memory) | `practice/day18_todo.py` |
| 19 | Word counter for a text file | `practice/day19_wordcount.py` |
| 20 | A simple quiz program | `practice/day20_quiz.py` |
| 21 | Refactor: rewrite an earlier program using functions | `practice/day21_refactor.py` |

### Week 4 — Apply it to real work

| Day | Task | File |
|---|---|---|
| 22 | Read `simulator/sensor_simulator.py` in your ESP32 project and write notes | `days/day22.md` |
| 23 | Run the ESP32 project end to end; log what you saw | `days/day23.md` |
| 24 | Change one number in the simulator (the publish interval) and commit it | `days/day24.md` |
| 25 | Read `ml/train_model.py`; explain it in your own words | `days/day25.md` |
| 26 | Add a Celsius↔Fahrenheit helper to your own practice file | `practice/day26_helper.py` |
| 27 | Write a proper README for one of your practice programs | `practice/README.md` |
| 28 | Make a small change to the ESP32 dashboard and test it | `days/day28.md` |
| 29 | Write "what I learned in 30 days" | `days/day29.md` |
| 30 | Update your GitHub profile README with your progress | `days/day30.md` |

Days 22–30 deliberately point at your **esp32-environment-monitor** project —
by then you will be reading and changing real code, which is the whole point.

---

## How to commit each day (two ways)

**The easy way — in the browser, no setup needed:**

1. Open this repo on GitHub
2. Click **Add file → Create new file**
3. Name it (e.g. `practice/day05_loops.py`), type your code
4. Scroll down, write a commit message, click **Commit new file**

**The normal way — with Git installed:**

```bash
git add .
git commit -m "day 5: multiplication table with a for loop"
git push
```

Either is fine. The browser is perfect while you are starting.

---

## Rules

1. **20–40 minutes a day.** Small and daily beats long and occasional.
2. **One commit a day, minimum.** Even a few lines counts.
3. **The commit message says what you did** — "day 4: pass/fail check", not "update".
4. **Stuck? Write down what confused you** in the day's note and commit that.
   Confusion you wrote down is progress.
5. **Missing a day is fine — missing two is a habit.** If you miss one, just
   carry on; do not try to "catch up" with fake commits.

---

## Progress

See [PROGRESS.md](PROGRESS.md) to tick off each day.

---

*Started as a 30-day habit. Kept because it worked.*
