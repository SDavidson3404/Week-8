import random
guesses = 0
correct = False
# Create a list of 10 numbers
numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Chooses a random number from the list
answer = random.choices(numList)
# Define a function to check if answer is correct
def answerCheck(guess, answer, correct):
    if answer == guess:
        print("You got it right!")
        correct = True
    else:
        print(f"You guessed incorrectly {2 - guesses} guesses left")
        correct = False
# give the user three guesses
while guesses < 3:
    userGuess = int(input("Please enter your guess: "))
    answerCheck(userGuess, answer, correct)
    if correct:
        break
    elif not correct:
        guesses += 1
