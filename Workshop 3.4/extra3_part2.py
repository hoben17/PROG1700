# TO DO
# Add a case that says `"Perfect!"` if score = 100.
# Add another condition that says `"Retake exam required"` if score < 40.

score = int(input("Enter your score (0–100): "))

if score >= 90:
    print("Excellent")
elif score >= 70:
    print("Good")
elif score >= 50:
    print("Pass")
else:
    print("Fail")