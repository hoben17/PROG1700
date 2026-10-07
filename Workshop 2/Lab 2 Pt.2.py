# Step 1: Get your name and age
name = input("Enter your name: ")
age_text = input("Enter your age: ")


if age_text.isdigit():
        next_year_age = int(age_text) + 1
        print(f"hello {name}, next year you will be {next_year_age} years old.")
else:
        print("invalid age input. Please enter a numeric value for age.")
