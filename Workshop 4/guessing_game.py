
print("Welcome to the Number Guessing Game!")

import random

secret = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

print("Your guess:", guess)
print("Secret number:", secret)
