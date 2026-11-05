number_of_grades = int(input("How many grades? "))

total = 0
pass_count = 0
fail_count = 0

for student_number in range(1, number_of_grades +1):
    print("student", student_number)

    grade = int(input("Enter grade: "))

    total = total + grade

    if grade >= 50:
        pass_count = pass_count + 1
    else:
        fail_count = fail_count + 1

average = total / number_of_grades

print("Number of grades:", number_of_grades)
print("Average grade:", average)
print("Passing grades", pass_count)
print("Failing grades:", fail_count)
