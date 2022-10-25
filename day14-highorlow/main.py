import random

from game_data import data

def assign():
    # Select an option from game_data
    return random.choice(data)

def compare_winner(p1, p2, user_choice):
    # Compare the winner 

    # store the follower count of account1 in a variable
    sum1 = p1['follower_count']
    # store the follower count of account1 in a variable
    sum2 = p2['follower_count']

    # Make an empty variable where
    # we store the name of the account
    # with the highest followers 
    max = ""

    # If account2 has more followers
    if sum1 < sum2:
        max = p2["name"]
    # if account2 has more followers
    elif sum1 > sum2:
        max = p1["name"]
    
    # Compare it with user choice
    if max == user_choice:
        return True
    else:
        return False

def play():
    # Function to play the game
    # infinite loop
    # game again and again
    continue_play = True
    while continue_play:

        # Variable to keep track of user's score
        # how many time user has answer correctly
        score = 0

        # Infinite loop to keep current game play
        still_guessing = True

        while still_guessing:
            # assign two accounts name to display
            person1 = assign()
            person2 = assign()
            
            # If we are not in first iteration, and user 
            # input correct answer to previous iteration,
            # in that case, make accoun1 become accoun2
            # and randomly assign account2 some other account
            if score > 0:
                person1 = person2
                person2 = assign()

                if person1 == person2:
                    person2 = assign()
            
            # display account1 name and description
            print(f"Name: {person1['name']}, Desc: {person1['description']}")
            print("-------VS--------------VS--------------VS--------------VS")
            print("--------------VS--------------VS--------------VS---------")
            # display account2 name and description
            print(f"Name: {person2['name']}, Desc: {person2['description']}")

            print(f"----------------Your current score is: {score}----------------")
            
            # ask for user input
            user_input = input("Please choose the Name which one would have the highest followers: ")

            # Check if user is correct
            if compare_winner(person1, person2, user_input):

                score += 1
            else:
                still_guessing = False
                print(f"Your final score is: {score}")

        # if user wants to continue, otherwise end the outer loop
        # check if the user entered some other input
        play_again = input("Do you wish to play again y/n: \n").lower()

        if play_again == 'y':
            continue
        elif play_again == 'n':
            continue_play = False
            print("Program exited")
        else:
            print("Invalid input: Exit Game!")

            


want_to_play = input("Do you want to play Higher or Lower y/n \n").lower()

if want_to_play == 'y':
    play()
elif want_to_play == 'n':
    print("Program exited successfully!")
else:
    print("Invalid input: Program exited")
