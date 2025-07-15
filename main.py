
questions = [
    {"question": "Hello! What is your name?: ", "responseType": str},
    {"question": "What's your age?: ", "responseType": int},
    {"question": "Which camp do you want to go to?: ", "responseType": int},
    {"question": "Would you like to take the shuttle bus ($80)? (y/n): ", "responseType": str},
    {"question": "What meal option would you like? (standard/vegetarian/vegan): ", "responseType": str}
]

answers = [0] * 5 # Fill the answers array with 5 zeros representing each questions answer
answersComplete = False

while not answersComplete:

    currentQuestion = answers.index(0) # Locates the first variable that is zero and stores the index

    temp = input(questions[currentQuestion]["question"])

    if (questions[currentQuestion]["responseType"] == int):
        try:
            answers[currentQuestion] = int(temp)
        except ValueError:
            print("You must enter a valid number")
    else:
        answers[currentQuestion] = temp


    if 0 not in answers: # Filling the answers list with 0's means we can do this simple check to see if we've finished
        confirmation = input(f"Confirm you are {answers[0]}, age {answers[1]} who has chosen camp {answers[2]}"
                            f" with {answers[4]} meals. (Y/n): ")

        if confirmation.lower() == "y":
            print("Thank you for confirming! Enjoy your trip!")
            answersComplete = True
        else:
            print("Ok. Lets try that again!")
            answers = [0] * 5

print(answers)