
import random

secret = 5
invalid_attempts = 0
invalid_attempts += 1

while True:
    try:
        guess = int(input("Guess a number between 1 and 10: "))
    except ValueError:
        invalid_attempts += 1
        print("That is not a whole number. Please try again.")
        continue

    if not 1 <= guess <=10:
        invalid_attempts += 1
        print("Out of range. Enter a number from 1 to 10.")

    if guess < secret:
        print("too low")
    elif guess > secret:
        print("Too high")
    else:
        print("You got it!")
        print(invalid_attempts)
        break
