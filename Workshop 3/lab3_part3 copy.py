
# TO DO:
# Change the code to warn only if temperature is **below 0 AND raining
# 

temp = float(input("Enter the temperature (°C): "))

if temp < 0 or temp > 35:
    print("Warning: Extreme temperature!")
else:
    print("Temperature is normal.")