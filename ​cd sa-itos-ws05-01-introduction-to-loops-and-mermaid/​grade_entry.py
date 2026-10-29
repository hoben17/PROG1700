count = 0

try:
    grade = int(input("Enter a grade (0-100), or -1 to finish: "))

    while grade != -1:
        if 0<= grade <=100:
            print("Accepted grade:", grade)
            count += 1
            total += grade
       
        else:
            print("Invalid grade. Enter 0-100 or -1 to finish. ")

        grade = int(input("Enter a grade (0-100), or -1 to finish: "))

except ValueError:
    print("please enter a valid grade")
    if count > 0:
        average = total / count
        print(f"Average: {average:.2f}")

print("Number of accepted grades:", count)
