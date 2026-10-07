# PROG1700 – Logic & Programming

**Instructor:** Davis Boudreau
**Week 3 – Workshop: Letter Grade Calculator**

---

## 🎯 Learning Goals

* Apply **multi-branch decision making** using `if/elif/else`.
* Translate a **use case into pseudocode**.
* Use **trace tables** to test multiple inputs and edge cases.
* Reflect on problem-solving strategies and coding process.

---

## 📝 Use Case: **Letter Grade Calculator**

A college course assigns letter grades based on a numeric score (0–100). The grading rules are:

* **90–100 → A**
* **80–89 → B**
* **70–79 → C**
* **60–69 → D**
* **0–59 → F**
* Anything below 0 or above 100 → Invalid

**Your task:**
Write a program that:

1. Prompts the user for their numeric grade.
2. Outputs the correct letter grade.

---

## 🔹 Step 1: Write Pseudocode

```
START
PROMPT user for numeric grade
READ grade
IF grade < 0 OR grade > 100 THEN
    DISPLAY "Invalid grade"
ELSE IF grade >= 90 THEN
    DISPLAY "A"
ELSE IF grade >= 80 THEN
    DISPLAY "B"
ELSE IF grade >= 70 THEN
    DISPLAY "C"
ELSE IF grade >= 60 THEN
    DISPLAY "D"
ELSE
    DISPLAY "F"
ENDIF
END
```

---

## 🔹 Step 2: Build a Trace Table

| **Input (Grade)** | **Condition True?** | **Output** |
| ----------------- | ------------------- | ---------- |
| -10               | grade < 0           | Invalid    |
| 95                | grade >= 90         | A          |
| 83                | grade >= 80         | B          |
| 74                | grade >= 70         | C          |
| 62                | grade >= 60         | D          |
| 50                | else                | F          |
| 105               | grade > 100         | Invalid    |

---

## 🔹 Step 3: Python Solution

```python
# Letter Grade Calculator

grade = int(input("Enter your numeric grade (0-100): "))

if grade < 0 or grade > 100:
    print("Invalid grade")
elif grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")
```

---

## 🔹 Step 4: Challenge Extension

* Add a **+ or - modifier**:

  * 97–100 → A+
  * 93–96 → A
  * 90–92 → A-
* Apply similar logic for **B, C, D** ranges.

---

## ✅ Deliverables

By the end of this lab, you should submit:

1. **Pseudocode** for the use case.
2. A **completed trace table** (at least 5 test cases).
3. A **working Python script** that implements the grade calculator.
4. Optional: an **extended version** with `+/-` modifiers.

---

## 💡 Reflection

Answer the following in **3–4 sentences**:

* What was the **hardest part** of writing the pseudocode?
* How did the **trace table** help you catch mistakes before coding?
* If you had to explain this problem to a friend new to coding, how would you break it down?
