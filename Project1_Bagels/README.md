# Deductive Logic Game
## Overview
This Python program is a simple text-based game that challenges the player to guess a 3-digit number chosen by the computer. The player is given a limited number of attempts and receives hints to guide their guesses.

## How to Play
1. Run the program by executing the code in a Python environment.
2. You will be informed that the computer has chosen a 3-digit number.
3. You will have a maximum number of attempts (specified when creating an instance of the game) to guess the number.
4. Enter a 3-digit number as your guess.
5. The program will provide you with hints:
    - "Pico" means one digit is correct but in the wrong position.
    - "Fermi" means one digit is correct and in the right position.
    - "Bagels" means none of the digits are correct.
6. Continue guessing until you either:
    - Correctly guess the number, in which case you win.
    - Use up all your attempts, in which case you lose, and the computer reveals the secret number.
7. After each game, you will be asked if you want to play again.
## Example
Here's an example of what a game session might look like:

I have chosen a 3-digit number. See if you can guess it! I will give you hints:

When I say "Pico", it means one digit is correct but in the wrong position.
When I say "Fermi", it means one digit is correct and in the right position.
If I say "Bagels", none of the digits are correct.

I have got the number in mind, and you have 10 attempts to figure it out.

        Guess no. 1 : 123
        Pico

        Guess no. 2 : 456
        Bagels

        Guess no. 3 : 789
        Bagels

        ...

        Guess no. 10 : 567
        Bagels
        Your are out of guess 
        Secret Numer : 321

        Do you want to play again? yes/no : no
## Customization
You can customize the game by changing the max_guess variable in the code. This variable controls the maximum number of attempts the player has.

Feel free to modify and enhance the code to add more features or improve the user experience.

Enjoy playing the Deductive Logic Game!