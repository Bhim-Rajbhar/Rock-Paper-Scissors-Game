################### Rock Paper Scissors Game ################################3

import random  # Importing the random module to generate random choices

# Welcome message
print("Welcome to Bhim's Rock Paper Scissors Game.\n")

# ASCII art for different choices: Rock, Paper, Scissors
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

# List containing ASCII art for each choice
game_images = [rock, paper, scissors]

# Prompting the user to choose rock, paper, or scissors
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
print(game_images[user_choice])  # Displaying the user's choice using the corresponding ASCII art

# Generating a random choice for the computer
computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])  # Displaying the computer's choice using the corresponding ASCII art

# Logic for determining the winner
if user_choice >= 3 or user_choice < 0: 
    print("You typed an invalid number, you lose!")  # If the user input is invalid
elif user_choice == 0 and computer_choice == 2:
    print("You win!")  # If user chooses Rock and computer chooses Scissors
elif computer_choice == 0 and user_choice == 2:
    print("You lose")  # If computer chooses Rock and user chooses Scissors
elif computer_choice > user_choice:
    print("You lose")  # If computer's choice beats user's choice
elif user_choice > computer_choice:
    print("You win!")  # If user's choice beats computer's choice
elif computer_choice == user_choice:
    print("It's a draw")  # If both choices are the same, it's a draw
