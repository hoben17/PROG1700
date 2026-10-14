# TO DO
# Add a condition: If `raining == "yes"` and `cold == "yes"` **and** user enters `"windy"`, print `"Stay inside!"

raining = input("Is it raining? (yes/no): ")
cold = input("Is it cold outside? (yes/no): ")

if raining == "yes" and cold == "yes":
    print("Wear a raincoat and warm clothes.")
elif raining == "yes" and cold == "no":
    print("Take an umbrella.")
elif raining == "no" and cold == "yes":
    print("Wear a jacket.")
else:
    print("Enjoy the nice weather!")