# Today imma build a simple number geusser using python.

import random
notDone = True
while (notDone):
    userChoice = input("Do you wanna be the one to guess the number or do you want me to guess the number? (Type 'me' or 'you') ")

    if userChoice.lower() == "me":
        randomNumber = random.randint(1, 100)
        

        print("I have chosen a number between 1 and 100. Try to guess it!")
        while True:
            userGuess = int(input("Enter your guess: "))
            
            if userGuess == randomNumber:
                print("Congratulations! You guessed the number.")
                break
            elif userGuess < randomNumber:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
    elif userChoice.lower() == "you":
        print("Think of a number between 1 and 100, and I will try to guess it.")
        low = 1
        high = 100
        while True:
            computerGuess = random.randint(low, high)
            userFeedback = input(f"My guess is {computerGuess}. Is it too high (h), too low (l), or correct (c)? ")
            if userFeedback.lower() == "c":
                print("Yay! I guessed your number.")
                break
            elif userFeedback.lower() == "h":
                high = computerGuess - 1
            elif userFeedback.lower() == "l":
                low = computerGuess + 1
            else:
                print("Invalid input. Please respond with 'h', 'l', or 'c'.")
    notDone = input("Would you like to play again? (yes/no) ").lower() == "yes"
    if not notDone:
        print("Thanks for playing! Goodbye!")



# Simple project to practice basic programming concepts like loops, conditionals, and user input.