#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from random import *

computer_target = randint(1, 100)

print("Welcome to the number Guessing Game!\n I am thinking of a number between 1 and 100. \n")

difficult = input("Choose a difficulty. Type 'easy' or 'hard'").lower()

def count(counts, attempts):
    user_guess = int(input("Enter a number between 1 and 100: "))
    print(f"User Picked: {user_guess}")
    count = 1
    no_of_guess = False
    print(f"You have {attempts} attempts remaining to guess the number.\n")
    while no_of_guess == False and count <= counts: 
       user_guess = int(input("Make a guess: "))
       if computer_target == user_guess:
         print(f"You guessed correct, number is: {computer_target} ")
         no_of_guess = True

       elif user_guess < computer_target:
        print(f"Too low! Guess Again ")
        count +=1
        attempts -= 1
        print(f"You have {attempts} left")

       elif user_guess > computer_target:
        print(f"Too High! Guess again")
        count +=1
        attempts -= 1
        print(f"You have {attempts} left")

if difficult == 'hard':
    count(5, 5)
elif difficult == 'easy':
    count(10, 10)

