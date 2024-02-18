# Rock-Paper-Scissors-Game

1. Importing the random Module: The random module is imported to generate random choices for the computer player.

2. Welcome Message: The code prints a welcome message to the player.

3. ASCII Art for Choices: ASCII art representations of the game choices (rock, paper, scissors) are defined using multi-line strings (rock, paper, scissors).

4. List of Game Images: The ASCII art representations are stored in a list called game_images.

5. User Input: The player is prompted to choose their option (Rock, Paper, or Scissors) by entering a number (0 for Rock, 1 for Paper, or 2 for Scissors). The input is converted to an integer using int(input(...)) and stored in user_choice.

6. Validation of User Input: The code checks if the user input is valid (i.e., within the range 0 to 2). If the input is invalid, an error message is printed.

7. Displaying User's Choice: If the user input is valid, the ASCII art representation of the user's choice is displayed based on the index entered by the user.

8. Computer's Choice: The computer's choice is generated randomly using random.randint(0, 2) to select a random index corresponding to Rock, Paper, or Scissors.

9. Displaying Computer's Choice: The ASCII art representation of the computer's choice is displayed.

10. Determining the Winner: The code compares the choices made by the user and the computer to determine the winner based on the rules of the game:

- If the user wins, a message "You win!" is printed.
- If the computer wins, a message "You lose" is printed.
- If it's a draw, a message "It's a draw" is printed.
- This process determines the outcome of a single round of the Rock, Paper, Scissors game and provides the result to the player.

Reference from : https://wrpsa.com/
