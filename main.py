NAME_INDEX = 0
AGE_INDEX = 1
CAMP_INDEX = 2
SHUTTLE_INDEX = 3
MEAL_INDEX = 4

ANSWER_LIST_SIZE = 5

LIST_ZERO_SYMBOL = None

AGE_LOWER_LIMIT = 5
AGE_UPPER_LIMIT = 17

CAMP_LEADER_AGE = 15

questions = [
    {"question": "Hello! What is your name?: ", "responseType": str},
    {"question": "What's your age?: ", "responseType": int},
    {"question": "Which camp do you want to go to? (1: Cultural Immersion, 2: Kayaking & Pancakes, 3: Mountain Biking): ", "responseType": int},
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
            if (int(temp) < AGE_LOWER_LIMIT or int(temp) > AGE_UPPER_LIMIT) and currentQuestion == AGE_INDEX: # Age check
                print(f"You must be 5-17 years of age to attend this camp {answers[NAME_INDEX]}.")
                break
            elif (int(temp) not in (1,2,3)) and currentQuestion == CAMP_INDEX: # 1,2 and 3 represent each camp
                print("You must select either: 1, 2 or 3")
            else:
                answers[currentQuestion] = int(temp)
        except ValueError:
            print("You must enter a valid number")
    else:
        if currentQuestion == NAME_INDEX and temp.lower().isalpha():
            answers[currentQuestion] = temp
        elif currentQuestion == SHUTTLE_INDEX and temp.lower() in ("y", "n"):
            answers[currentQuestion] = temp
        elif currentQuestion == MEAL_INDEX and temp.lower() in ("standard", "vegetarian", "vegan"):
            answers[currentQuestion] = temp
        else:
            print("Sorry that input was invalid please try again.")

    if LIST_ZERO_SYMBOL not in answers:

        if answers[AGE_INDEX] >= CAMP_LEADER_AGE: # Executes if inputted age is greater than 15
            campLeader = input("You are eligible to be the camp leader! Would you like to sign up as one? (y/n): ")
            if campLeader.lower() == "y":
                campLeader = True
            else:
                del campLeader

        try:
            campLeader
        except NameError:
            confirmation = input(
                f"Confirm you are {answers[NAME_INDEX]}, age {answers[AGE_INDEX]} who has chosen camp {answers[CAMP_INDEX]}"
                f" with {answers[MEAL_INDEX]} meals. (Y/n): ")
        else:
            confirmation = input(
                f"Confirm you are {answers[NAME_INDEX]}, age {answers[AGE_INDEX]} who has chosen camp {answers[CAMP_INDEX]}"
                f" with {answers[MEAL_INDEX]} meals and has chosen to be camp leader. (Y/n): ")

        if confirmation.lower() == "y":
            print("Thank you for confirming! Enjoy your trip!")
            answersComplete = True
        else:
            print("Ok. Lets try that again!\n------------------------")
            answers = [LIST_ZERO_SYMBOL] * ANSWER_LIST_SIZE # Reset the answers list for the program to run again

print(answers)