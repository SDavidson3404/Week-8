# Function to convert Celsius to Farenheit
def conversion(temp):
    tempConverted = (temp * 9/5) + 32
    return tempConverted

# Stores three user input temperatures as variables
tempC = int(input("Please enter a temperature in Celsius: "))
tempC2 = int(input("Please enter a second temperature in Celsius: "))
tempC3 = int(input("Please enter a third and final temperature in Celsius: "))
# Converts the temps to Farenheit and stores them in other variables
tempF = conversion(tempC)
tempF2 = conversion(tempC2)
tempF3 = conversion(tempC3)
# Print both F and C temps
print(f"""Temp 1: {tempF}F or {tempC}C
Temp 2: {tempF2}F or {tempC2}C
Temp 3: {tempF3}F or {tempC3}C""")
# Store both F and C to file
with open("Temps.txt", "w") as file:
    file.write(f"""Temp 1: {tempF}F or {tempC}C
Temp 2: {tempF2}F or {tempC2}C
Temp 3: {tempF3}F or {tempC3}C""")
