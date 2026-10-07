# PROG1700 – Logic & Programming

**Instructor:** Davis Boudreau
**Week 3 – Workshop: Simple ATM Withdrawal Simulator**

---

## 🎯 Learning Goals

* Apply **multi-branch decision making** with `if/elif/else`.
* Translate a **real-world transaction scenario into pseudocode**.
* Use **trace tables** to test logic for various input scenarios.
* Reflect on problem-solving strategies and coding process.

---

## 📝 Use Case: **ATM Withdrawal Simulator**

Write a program that:

1. Prompts the user to enter their **current account balance** and the **amount to withdraw**.
2. Checks if the withdrawal amount is valid:

   * Withdrawal cannot exceed the balance.
   * Withdrawal cannot be negative or zero.
3. Displays:

   * If valid, the **new balance**.
   * If invalid, an **error message** explaining why the transaction failed.

**Example:**

| Balance | Withdraw | Output                    |
| ------- | -------- | ------------------------- |
| 500     | 200      | New balance: 300          |
| 500     | 600      | Error: Insufficient funds |
| 500     | -50      | Error: Invalid withdrawal |

---

## 🔹 Step 1: Pseudocode

```
START
PROMPT user for account_balance
READ account_balance
PROMPT user for withdraw_amount
READ withdraw_amount

IF withdraw_amount <= 0 THEN
    DISPLAY "Error: Invalid withdrawal"
ELSE IF withdraw_amount > account_balance THEN
    DISPLAY "Error: Insufficient funds"
ELSE
    account_balance = account_balance - withdraw_amount
    DISPLAY "New balance:", account_balance
ENDIF
END
```

---

## 🔹 Step 2: Trace Table

| Balance | Withdraw | Condition Checked    | Output                    |
| ------- | -------- | -------------------- | ------------------------- |
| 500     | 200      | 200>0 and 200<=500   | 300                       |
| 500     | 600      | 600>500 → true       | Error: Insufficient funds |
| 500     | -50      | -50<=0 → true        | Error: Invalid withdrawal |
| 0       | 10       | 10>0 but 10>0 → true | Error: Insufficient funds |
| 1000    | 0        | 0<=0 → true          | Error: Invalid withdrawal |

---

## 🔹 Step 3: Python Solution

```python
# Simple ATM Withdrawal Simulator

account_balance = float(input("Enter your current balance: "))
withdraw_amount = float(input("Enter amount to withdraw: "))

if withdraw_amount <= 0:
    print("Error: Invalid withdrawal")
elif withdraw_amount > account_balance:
    print("Error: Insufficient funds")
else:
    account_balance -= withdraw_amount
    print("New balance:", account_balance)
```

---

## 🔹 Step 4: Challenge Extension

* Add a **daily withdrawal limit** (e.g., $500/day).
* Include **multiple withdrawal attempts**, updating the balance each time.
* Display a **receipt** showing previous balance, withdrawal amount, and new balance.

---

## ✅ Deliverables

Submit the following:

1. **Pseudocode** for the ATM logic.
2. **Completed trace table** with at least 5 test cases including edge cases.
3. A **working Python script** implementing the withdrawal logic.
4. Optional: **extended version** with daily limits or receipt printout.

---

## 💡 Reflection

Answer the following in **3–4 sentences**:

* How did planning with **pseudocode** help you handle multiple error conditions?
* Which scenario in your trace table was most useful for debugging?
* How would you explain the **decision logic** to someone unfamiliar with programming?

