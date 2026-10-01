![alt text](NSCC-ITOS-Wordmark.png)

---

# Lab: Basic Syntax & Data Types — Console I/O and Simple Validation

**Course:** PROG1700 — Logic & Programming
**Time:** \~2 hours

---

## Learning Goals

By the end of this lab, you will be able to:

* Use **variables** and basic <b>data types</b> (string, int, float).
* Get user input with `input()`.
* Convert strings to numbers using `int()` and `float()`.
* Print results using **f-strings**.
* Do **very simple validation** using `if` statements.

---

# Step-by-Step Activities

---

## 1. Variables and Types

**Task:** Create a file `lab2_part1.py`.

Write this code:

```python
name = "Alex"
age = 21
height = 1.75   # in meters

print(name)
print(age)
print(height)

print(type(name))
print(type(age))
print(type(height))
```

👉 Run it. You should see the values and their data types.

**Exercise:**

* Change the values (your name, your age, your height).
* Add a new variable `is_student = True` and print it.

---

## 2. Input and Conversion

**Task:** Create `lab2_part2.py`.

```python
name = input("Enter your name: ")
age_text = input("Enter your age: ")
age = int(age_text)   # convert string to int

print(f"Hello {name}, next year you will be {age + 1} years old.")
```

**Exercise:**

* Try entering a number for age (works fine).
* Try typing words like `"ten"`. What happens? (Hint: error message)

---

## 3. Very Simple Validation

**Task:** Improve `lab2_part2.py` so it checks if the age looks like a number before converting.

```python
age_text = input("Enter your age: ")

if age_text.isdigit():
    age = int(age_text)
    print(f"In 5 years you will be {age + 5}.")
else:
    print("That doesn't look like a number.")
```

**Exercise:**

* Run it with `20` → should work.
* Run it with `"twenty"` → should show error.

---

## 4. Working with Numbers

**Task:** Create `lab2_part3.py`.

```python
num1_text = input("Enter the first number: ")
num2_text = input("Enter the second number: ")

num1 = float(num1_text)
num2 = float(num2_text)

total = num1 + num2
average = total / 2

print(f"Total = {total}")
print(f"Average = {average}")
```

**Exercise:**

* Try entering `3` and `7`.
* Try entering decimal numbers (like `2.5`).

---

## 5. Mini Challenge – Receipt Program

**Task:** Create `receipt.py`.

* Ask the user for 3 items (name + price).
* Print the items and the total.

**Starter code:**

```python
item1 = input("Enter first item: ")
price1 = float(input("Enter price of first item: "))

item2 = input("Enter second item: ")
price2 = float(input("Enter price of second item: "))

item3 = input("Enter third item: ")
price3 = float(input("Enter price of third item: "))

total = price1 + price2 + price3

print("----- Receipt -----")
print(item1, ":", price1)
print(item2, ":", price2)
print(item3, ":", price3)
print("Total:", total)
```

👉 Try running it and enter your own items.

---

## Reflection

Write 3–4 sentences:

* What happens when you forget to convert input to numbers?
* What’s the difference between `int()` and `float()`?
* Why do we validate input?

---

## Deliverables

Upload to your GitHub repo under `week2/`:

* `lab2_part1.py`
* `lab2_part2.py`
* `lab2_part3.py`
* `receipt.py`
* Reflection text file
