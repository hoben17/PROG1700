
import random

secret = random.randint(1, 10)

while True:
    # 1. Retrieve input as text.
    raw_guess = input("Guess a number between 1 and 10: ").strip()

    # 2. Validate the text before conversion.
    if not raw_guess.isdigit():
        print("Please enter a whole number using digits 0–9.")
        continue

    # 3. Convert after checking the text.
    guess = int(raw_guess)

    # 4. Check the game's allowed range.
    if not 1 < guess <= 10:
        print("Out of range. Enter a number from 1 to 10.")
        continue

    # 5. Compare only accepted guesses with the secret.
    if guess < secret:
        print("Too low! 📉")
    elif guess > secret:
        print("Too high! 📈")
    else:
        print("You got it! 🎉")
        break