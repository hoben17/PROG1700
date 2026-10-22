
while True:
    try:
        raw_value = input("Enter a whole number: ")
        number = int(raw_value)
        print("Accepted:", number)
        break
    except ValueError:
        print("Please try again using a whole number.")

print("Input accepted. Continuing...")

# LEFT OFF AT CHALLENGE 7