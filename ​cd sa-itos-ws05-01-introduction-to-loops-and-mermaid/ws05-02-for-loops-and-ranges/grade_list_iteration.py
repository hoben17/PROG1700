grades = [100, 75, 20, 90, 85]

total = 0

for grade in grades:
    print("Processing grade:", grade)
    total = total + grade

average = total / len(grades)

if average >= 50:
    print("Pass")
else:
    print("Fail")

print("Number of Grades:", len(grades))
print("Total:", total)
print("Average:", average)
