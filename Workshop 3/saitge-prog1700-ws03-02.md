# PROG1700 – Logic & Programming

**Instructor:** Davis Boudreau
**Week 3 – Conditional Logic Workshop**

---

## 📝 Use Case: **Bus Fare Calculator**

A local transit system charges different fares depending on the rider’s age:

* **Children (0–12):** Free
* **Teenagers (13–17):** $2.00
* **Adults (18–64):** $3.50
* **Seniors (65+):** $1.50

Write a program that:

1. Asks the user for their age.
2. Determines the correct fare.
3. Displays the fare in a clear message.

---

## Step 1: Pseudocode

```
START
PROMPT user for age
READ age
IF age < 0 THEN
    DISPLAY "Invalid age"
ELSE IF age <= 12 THEN
    DISPLAY "Fare is Free"
ELSE IF age <= 17 THEN
    DISPLAY "Fare is $2.00"
ELSE IF age <= 64 THEN
    DISPLAY "Fare is $3.50"
ELSE
    DISPLAY "Fare is $1.50"
ENDIF
END
```

---

## Step 2: Trace Table

Let’s test the decision logic for a few values.

| **Input (Age)** | **Condition True?** | **Output**      |
| --------------- | ------------------- | --------------- |
| -5              | age < 0             | "Invalid age"   |
| 10              | age <= 12           | "Fare is Free"  |
| 15              | age <= 17           | "Fare is $2.00" |
| 35              | age <= 64           | "Fare is $3.50" |
| 70              | else (65+)          | "Fare is $1.50" |

---

## Step 3: Python Solution

```python
# Bus Fare Calculator

age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age")
elif age <= 12:
    print("Fare is Free")
elif age <= 17:
    print("Fare is $2.00")
elif age <= 64:
    print("Fare is $3.50")
else:
    print("Fare is $1.50")
```

---

## Step 4: Challenge Extension

* Modify the program so it asks if the rider is a **student** (Y/N).

  * If a student is between **18–25**, apply a **discount fare of $2.00** instead of $3.50.

---

👉 This exercise shows students how to:

* Translate a **real-world rule system** into conditional logic.
* Use **multi-branch `if/elif/else`** statements.
* Validate input and test with a **trace table**.
