# Lab: Conditional Logic and Branching

**Course:** PROG1700 — Logic & Programming
**Week:** 3
**Time:** \~2 hours

---

## 🎯 Learning Goals

By the end of this lab, you will be able to:

* Write programs using `if`, `elif`, and `else`.
* Combine conditions with **and/or/not**.
* Use **nested conditions** when needed.
* Trace logic with a simple **truth table**.
* Solve small decision-making problems in code.

---

# Step-by-Step Activities

---

## Part 1 — Basic If/Else

**Task:** Create `lab3_part1.py`.

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

👉 Run it with different ages.

**Exercise:**

* Change the cutoff to 21 instead of 18.
* What happens if you enter `18` exactly?

---

## Part 2 — If / Elif / Else

**Task:** Create `lab3_part2.py`.

```python
score = int(input("Enter your test score (0-100): "))

if score >= 90:
    print("Grade = A")
elif score >= 80:
    print("Grade = B")
elif score >= 70:
    print("Grade = C")
elif score >= 60:
    print("Grade = D")
else:
    print("Grade = F")
```

**Exercise:**

* Try inputs `95`, `75`, and `50`.
* Add one more category: print `"Perfect score!"` if score = 100.

---

## Part 3 — Combining Conditions (and/or/not)

**Task:** Create `lab3_part3.py`.

```python
temp = float(input("Enter the temperature (°C): "))

if temp < 0 or temp > 35:
    print("Warning: Extreme temperature!")
else:
    print("Temperature is normal.")
```

**Exercise:**

* Change the code to warn only if temperature is **below 0 AND raining**.
* (Hint: use `and`).

---

## Part 4 — Nested Conditions

**Task:** Create `lab3_part4.py`.

```python
user = input("Enter username: ")
password = input("Enter password: ")

if user == "admin":
    if password == "1234":
        print("Access granted.")
    else:
        print("Wrong password.")
else:
    print("Unknown user.")
```

**Exercise:**

* Add a second valid username/password pair (e.g., `"student"` / `"pass"`).

---

## Part 5 — Trace Table Practice

Consider this code:

```python
x = 7
y = 3

if x > 5 and y < 5:
    print("Case 1")
elif x < 5:
    print("Case 2")
else:
    print("Case 3")
```

**Task:** Make a trace table for 3 different sets of `x` and `y`. Example format:

| x | y | Condition tested            | Output |
| - | - | --------------------------- | ------ |
| 7 | 3 | x > 5 and y < 5 → True/True | Case 1 |
| 2 | 3 | x > 5 → False               | Case 2 |
| 6 | 9 | x > 5 → True, y < 5 → False | Case 3 |

---

## Part 6 — Mini Challenge: Movie Ticket Pricing

**Task:** Create `lab3_ticket.py`.

* Ask the user for their **age**.
* Ticket prices:

  * Age < 5 → free
  * Age 5–12 → \$8
  * Age 13–64 → \$12
  * Age 65+ → \$6
* Print the ticket price.

**Extension:**

* Add a student discount: if age ≥ 13 and user enters `"yes"` for student, reduce price by \$2.

---

## Reflection

Answer in a text file `week3_reflection.txt`:

* Which was harder: simple if/else or nested if statements? Why?
* Why might trace tables help when debugging logic errors?

---

## ✅ Deliverables

Upload to GitHub under `week3/`:

* `lab3_part1.py`
* `lab3_part2.py`
* `lab3_part3.py`
* `lab3_part4.py`
* `lab3_ticket.py`
* `week3_reflection.txt`

