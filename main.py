NAME_INDEX = 0
AGE_INDEX = 1
CAMP_INDEX = 2
MEAL_INDEX = 4

ANSWER_LIST_SIZE = 5

LIST_ZERO_SYMBOL = 0

questions = [
    {"question": "Hello! What is your name?: ", "responseType": str},
    {"question": "What's your age?: ", "responseType": int},
    {"question": "Which camp do you want to go to?: ", "responseType": int},
    {"question": "Would you like to take the shuttle bus ($80)? (y/n): ", "responseType": str},
    {"question": "What meal option would you like? (standard/vegetarian/vegan): ", "responseType": str}
]

answers = [LIST_ZERO_SYMBOL] * ANSWER_LIST_SIZE # Fill the answers array with ANSWER_LIST_SIZE amount of LIST_ZERO_SYMBOL symbols representing each questions answer
answersComplete = False

while not answersComplete:

    currentQuestion = answers.index(LIST_ZERO_SYMBOL) # Locates the first variable that is zero and stores the index

    temp = input(questions[currentQuestion]["question"]) # Finds the question related to the empty index we located earlier

    if (questions[currentQuestion]["responseType"] == int): # Checks if the user should've used a number or not
        try:
            answers[currentQuestion] = int(temp)
        except ValueError:
            print("You must enter a valid number")
    else:
        answers[currentQuestion] = temp # This runs if the input shouldn't be a int (TODO: Need to fix to ensure user doesn't input numbers in the text)


    if LIST_ZERO_SYMBOL not in answers: # Filling the answers list with 0's means we can do this simple check to see if we've finished
        confirmation = input(f"Confirm you are {answers[NAME_INDEX]}, age {answers[AGE_INDEX]} who has chosen camp {answers[CAMP_INDEX]}"
                            f" with {answers[MEAL_INDEX]} meals. (Y/n): ")

        if confirmation.lower() == "y":
            print("Thank you for confirming! Enjoy your trip!")
            answersComplete = True
        else:
            print("Ok. Lets try that again!")
            answers = [LIST_ZERO_SYMBOL] * ANSWER_LIST_SIZE # Reset the answers list for the program to run again

print(answers)