# Week 3 Extra Practice Lab: More Practice with Conditionals

**Course:** PROG1700 — Logic & Programming
**Supplemental Practice (Week 3.5)**
**Time:** \~1.5–2 hours

---

## 🎯 Learning Goals

By completing this extra lab, you will:

* Strengthen your use of `if`, `elif`, `else`.
* Practice combining conditions with **and/or/not**.
* Write nested conditionals for more complex logic.
* Build and use trace tables to test your code.

---

# Step-by-Step Activities

---

## Part 1 — Even or Odd?

**Task:** Create `extra3_part1.py`.

```python
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is even.")
else:
    print(num, "is odd.")
```

👉 Test with `7` and `12`.

**Exercise:**

* Modify it so the program also prints:

  * `"Positive"` if number > 0
  * `"Negative"` if number < 0
  * `"Zero"` if number = 0

---

## Part 2 — Grade Feedback

**Task:** Create `extra3_part2.py`.

```python
score = int(input("Enter your score (0–100): "))

if score >= 90:
    print("Excellent")
elif score >= 70:
    print("Good")
elif score >= 50:
    print("Pass")
else:
    print("Fail")
```

**Exercise:**

* Add a case that says `"Perfect!"` if score = 100.
* Add another condition that says `"Retake exam required"` if score < 40.

---

## Part 3 — Boolean Logic Practice

**Task:** Create `extra3_part3.py`.

```python
raining = input("Is it raining? (yes/no): ")
cold = input("Is it cold outside? (yes/no): ")

if raining == "yes" and cold == "yes":
    print("Wear a raincoat and warm clothes.")
elif raining == "yes" and cold == "no":
    print("Take an umbrella.")
elif raining == "no" and cold == "yes":
    print("Wear a jacket.")
else:
    print("Enjoy the nice weather!")
```

👉 Run different scenarios.

**Exercise:**

* Add a condition: If `raining == "yes"` and `cold == "yes"` **and** user enters `"windy"`, print `"Stay inside!"`.

---

## Part 4 — Nested Conditions: ATM Simulator 💳

**Task:** Create `extra3_part4.py`.

```python
pin = input("Enter PIN: ")

if pin == "4321":
    option = input("Choose (balance/withdraw): ")
    if option == "balance":
        print("Your balance is $500")
    elif option == "withdraw":
        amount = int(input("Enter amount: "))
        if amount <= 500:
            print("Withdrawal successful")
        else:
            print("Insufficient funds")
    else:
        print("Invalid option")
else:
    print("Wrong PIN")
```

**Exercise:**

* Add a **deposit option**.
* Make the PIN check allow **two attempts** before locking the user out.

---

## Part 5 — Trace Table Practice

Consider this code:

```python
x = 4
y = 10

if x > 5 or y < 5:
    print("Case 1")
elif x == 4 and y == 10:
    print("Case 2")
else:
    print("Case 3")
```

👉 Make a trace table for at least **three different values** of `x` and `y`.

---

## Part 6 — Mini Challenge: Pizza Order 🍕

**Task:** Create `extra3_pizza.py`.

* Ask the user if they want **small, medium, or large** pizza.
* Small = \$8, Medium = \$10, Large = \$12.
* Ask if they want **extra cheese (yes/no)** → add \$2 if yes.
* Ask if they want **delivery (yes/no)** → add \$3 if yes.
* Print the **final price**.

**Extension:**

* If order is large AND has cheese AND delivery, print `"Big order discount: -$2"`.

---

## Reflection

Answer in `extra3_reflection.txt`:

* Which conditional structure (if/elif/else, nested if, or boolean operators) felt hardest to use?
* Did trace tables help you predict results before running the code?
* What new thing did you discover in this lab?

---

## ✅ Deliverables

Upload to GitHub under `extra_week3/`:

* `extra3_part1.py`
* `extra3_part2.py`
* `extra3_part3.py`
* `extra3_part4.py`
* `extra3_pizza.py`
* `extra3_reflection.txt`
