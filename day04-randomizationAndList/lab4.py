import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
choice = [rock, paper, scissors]
userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
print(choice[userChoice])
computerChoice= random.randint(0, 2)
print("Computer chose:")
print(choice[computerChoice])

# Quick rules: (0)rock beats (2)scissors, (2)scissors beats (1)paper, (1)paper beats (0)rock


if userChoice >= 3 or userChoice < 0: 
  print("You typed an invalid number, you lose!") 
elif userChoice == 0 and computerChoice == 2:
  print("You win!")
elif computerChoice == 0 and userChoice == 2:
  print("You lose")
elif computerChoice > userChoice:
  print("You lose")
elif userChoice > computerChoice:
  print("You win!")
elif computerChoice == userChoice:
  print("It's a draw")
