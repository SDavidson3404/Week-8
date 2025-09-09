# Take information as variables
name = input("Please enter your name: ")
age = input("Please enter your age: ")
city = input("Please enter your city: ")
# Open/Create a file and append info to it
with open("Info.txt", "w") as file:
    file.write(f"""Name: {name},
Age: {age}
city: {city}""")
# Tell the user the inputs
print(f"Hello, {name}, you are {age} years old and from {city}")
