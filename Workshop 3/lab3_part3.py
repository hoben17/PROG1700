
# TO DO:
# Change the code to warn only if temperature is **below 0 AND raining
# (Hint: use `and`)

temp = float(input("Enter the temperature (°C): "))
percip_input = input("Is it raining? (Y or y): ")
percip_input = bool

if percip_input == "y" or "Y":
    precip_status = True
else: 
    precip_status = False 
if temp < 0 or temp > 35:
    print("Warning: Extreme temperature!")
else:
    print("Temperature is normal.")