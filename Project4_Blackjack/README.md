# Blackjack Game
This is a Python implementation of the classic card game Blackjack. In this game, the player's goal is to reach a hand value as close to 21 as possible without exceeding it. The game is played against a computer dealer.

## Project Structure
The project consists of two Python files: blackjack.py and main.py. Below is an overview of each file's purpose and the functionality it provides:

**blackjack.py**
This file contains the implementation of the Blackjack game. It defines the BlackjackGame class, which handles the game's logic and rules.

**BlackjackGame Class**
The BlackjackGame class includes methods for various aspects of the game, including:

1. Initializing the game with a maximum bet amount.
2. Prompting the player for their bet amount.
3. Drawing random cards from the deck.
4. Displaying cards for the dealer and player.
5. Calculating the value of a hand of cards.
6. Allowing the player to make moves (Hit, Stand, Double Down).
7. Increasing the player's bet amount.
8. Evaluating the outcome of a round and updating the player's money.
9. Playing a round of Blackjack.

**game_introduction() Function**
Displays the rules and instructions for playing Blackjack.

**game_over_for_cheaters() Function**
Displays a message when the player runs out of chips and exits the game.

**main.py**
This file contains the main entry point for the game and provides functions for displaying game instructions and handling the game over scenario.


## Project Files
**blackjack.py:** Contains the implementation of the Blackjack game.

**main.py:** Provides the main entry point for the game, instructions, and game over handling.


## Code Structure
The code is organized into a Python class BlackjackGame, which contains various methods for playing the game. Here's an overview of the methods:

**__init__(self, max_bet):** Initializes the game with the maximum bet amount.
**get_bet(self):** Prompts the player for their bet amount.
**draw_deck(self):** Draws a random card from the deck.
**draw_cards(self, num):** Draws a specified number of cards.
**built_cards(self, hands, isfirst):** Prints a list of cards.
**calculate_cardvalue(self, card_values):** Calculates the value of a hand of cards.
**choose_move(self, money, cards):** Prompts the player for their next move.
**increase_bet(self, bet_val, money):** Increases the player's bet amount.
**display_cards(self, for_who, _card):** Displays a player's cards.
**card_result(self, dealer, player, userbet, money):** Evaluates the outcome of a round and updates the player's money.
**play_blackjack(self):** Plays a round of Blackjack.

The **game_introduction()** and **game_over_for_cheaters()** functions provide an introduction to the game and a message for when the player runs out of chips.

## How to Play
1. Run the main.py script to start the game.

2. Follow the on-screen instructions to place your bet and make moves (Hit, Stand, Double Down) during the game.

3. Try to beat the dealer by getting a hand value as close to 21 as possible without going over.

4. When the game is over, you will be prompted to continue playing or exit.

5. Enjoy the game and test your luck at beating the dealer!


Feel free to enjoy the game and have fun playing Blackjack!

Feel free to modify and improve the code or add more features to make it even more engaging.


