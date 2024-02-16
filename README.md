# Rock-Paper-Scissors-Game

1. Importing the random module: This allows the code to generate random choices, which is used to represent the computer's choice in the game.

2. ASCII Art: ASCII art representations of the choices (rock, paper, scissors) are defined using triple-quoted strings (rock, paper, scissors). These will be used to visually represent the choices made by the user and the computer.

3. The game_images list: This list contains the ASCII art representations of the choices. Each choice (rock, paper, scissors) corresponds to an index in the list.

4. User Input: The user is prompted to input their choice by entering a number (0 for Rock, 1 for Paper, or 2 for Scissors). This input is converted to an integer using int(input(...)).

5. Displaying the User's Choice: The ASCII art representation of the user's choice is displayed based on the index entered by the user. This is achieved by accessing the corresponding element in the game_images list.

6. Generating the Computer's Choice: The computer's choice is generated randomly using random.randint(0, 2). This generates a random integer between 0 and 2, inclusive, which corresponds to Rock, Paper, or Scissors.

7. Displaying the Computer's Choice: Similar to the user's choice, the ASCII art representation of the computer's choice is displayed based on the randomly generated index.

8. Determining the Winner:
The code then checks various conditions to determine the winner based on the game rules:
- If the user's input is invalid (not 0, 1, or 2), an error message is displayed.
- If the user wins (e.g., Rock crushes Scissors), a message "You win!" is displayed.
- If the computer wins (e.g., Rock crushes Scissors), a message "You lose" is displayed.
- If it's a draw (both user and computer chose the same option), a message "It's a draw" is displayed.

9. The game's outcome is displayed based on the comparison of choices made by the user and the computer.

Overall, this code provides a simple implementation of the classic Rock, Paper, Scissors game, incorporating ASCII art for a visually appealing interface.

Reference from : https://wrpsa.com/
