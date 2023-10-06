from blackjack import BlackjackGame

def game_introduction():
  print('''Welcome to Blackjack, a card game where the goal is to reach a hand value as close to 21 as possible without exceeding it. Here are the rules:

1. Face cards (Kings, Queens, and Jacks) are each worth 10 points.
2. Aces can be counted as either 1 or 11 points, depending on what benefits your hand.
3. Number cards (2 through 10) are worth their face value.
4. You have two main options during your turn:
  - (H)it: Take another card to improve your hand.
  - (S)tand: Stop taking cards and keep your current hand.
5. On your initial play, you can choose to (D)ouble down, which doubles your bet. However, you must take exactly one more card before standing.
6. In the event of a tie with the dealer, your bet is returned to you.
7. Feel free to enjoy the game and try your luck at beating the dealer!''')


def main():
  game_introduction()
  game = BlackjackGame(0)
  game.play_blackjack()


if __name__ == "__main__":
    main()
