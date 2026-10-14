

age = int(input("Enter your age: "))
student = input("Are you a student? (yes/no): ").strip().lower()

print(student)

if(student) and age == (18-25):
    input("bus fare $2.00")


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