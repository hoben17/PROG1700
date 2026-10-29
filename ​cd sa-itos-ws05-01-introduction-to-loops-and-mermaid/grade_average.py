count = 0
total = 0

while True:
    try:
        grade = int(input("Enter a grade (0-100), or -1 to finish: "))
        if grade == -1:
            break
        
        if 0 <= grade <= 100:
            print("Accepted grade:", grade)
            count += 1
            total += grade
        else:
            print("Invalid grade. Enter 0 to 100.")
    
    except ValueError:
        print("Please enter a valid grade.")

if count > 0:
    average = total / count 
    print(f"Average: {average:2f}")
else:
    print("No grades entered.")