x = 5
# Defines what "Add name" does
def addName():
    name = input("Please enter a name: ")
    with open("Names.txt", "a") as file:
        file.write(f"""{name}
""")
# Defines what "Show all names" does
def showNames():
    with open("Names.txt") as file:
        print(file.read())
# Gives user options
while x == 5:
    userChoice = int(input("""What would you like to do?
1. Add a name
2. Show all names
3. exit
"""))
    if userChoice == 1:
        addName()
    elif userChoice == 2:
        showNames()
    elif userChoice == 3:
        print("Have a good day!")
        break
# If input equals an option, do that option
