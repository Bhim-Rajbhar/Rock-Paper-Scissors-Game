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

# User input for their choice (0 for Rock, 1 for Paper, 2 for Scissors)
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

# Validation of user input
if user_choice >= 3 or user_choice < 0: 
    # If the user input is invalid
    print("You typed an invalid number, you lose!")  
else:
    # Displaying the user's choice
    print(game_images[user_choice])  

    # Generating computer's choice randomly
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    # Displaying the computer's choice
    print(game_images[computer_choice])  

    # Determining the winner
    if user_choice == 0 and computer_choice == 2:
        print("You win!")  
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")  
    elif computer_choice > user_choice:
        print("You lose")  
    elif user_choice > computer_choice:
        print("You win!")  
    elif computer_choice == user_choice:
        print("It's a draw")  
