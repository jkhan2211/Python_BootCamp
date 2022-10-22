from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5




#Function to check user's guess against actual answer
def check_answer(guess, answer, turns):
    """
    Checks answer against guess. Returns the number of turns remaining
    """
       #Track the number of turns and reduce by 1 if they get it wrong
    if guess > answer:
        print("Too High")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it. The answer is {answer}")

#Make function to set difficult 
def set_difficulty():
    level = input("Choose a difficulty: Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    #Choosing a random number between 1 and 100
    print("Welcome to the Number guessing Game!")
    print("Iam thinking of a number between 1 and 100")
    answer = randint(1, 100)
    print(f"The answer is {answer}-- comment this line")
    turns = set_difficulty()
    

    #Repeat the guessing functionality if they get it wrong
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")
        #Let the user guess a number
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print(f"You lost you have. Ran out of guesses. You Lose!")
            return
        elif guess != answer:
            print("Guess again!")



game()
 




