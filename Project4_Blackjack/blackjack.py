import  random


def game_over_for_cheaters():
  print('''\nYou've run out of chips!
It's a good thing this is just a game and not real money.
Thank you for playing!
Exiting the game now.''')

class BlackjackGame:

  def __init__(self, max_bet):
      """
      Initializes the Blackjack game with the maximum bet amount.

      Args:
          max_bet (int): The maximum bet amount allowed in the game.
      """
      self.max_bet = max_bet

  def get_bet(self):
    """
    Prompts the player for their bet amount.

    Returns:
        int: The player's bet amount.
    """
    while True:
        bet_val = input(f'\nEnter betting amount from your available funds [1-{self.max_bet}] or (Q)UIT: ')
        if bet_val.upper() == 'Q':
            print('THANKS FOR PLAYING!!!')
            return 0
        elif not bet_val.isdigit():
            print('\nEnter a correct integer bet amount.')
            continue
        elif 1 <= int(bet_val) <= self.max_bet:
            return int(bet_val)
        else:
            print(f'Enter an amount in range [1, {self.max_bet}]')

  def draw_deck(self):
    """
    Draws a random card from the deck.

    Returns:
        tuple: A tuple representing a card (rank, suit).
    """
    suits = ["\u2663", "\u2665", "\u2666", "\u2660"]
    ranks = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    return random.choice(ranks), random.choice(suits)

  def draw_cards(self, num):
    """
    Draws a specified number of cards.

    Args:
        num (int): The number of cards to draw.

    Returns:
        list: A list of tuples representing the drawn cards.
    """
    _hand = []
    for _ in range(num):
        _hand.append(self.draw_deck())
    return _hand

  def built_cards(self, hands, isfirst):
    """
    Prints a list of cards.

    Args:
        cards (list): A list of tuples representing the cards.
        is_first (bool): True if it's the first card to be displayed.
    """
    rows = ['', '', '', '', '']
    for i, hand in enumerate(hands):
      rows[0] += ' ___ '
      if isfirst:
        rows[1] += '|## | '
        rows[2] += '|###| '
        rows[3] += '|_##| '
        isfirst = False
      else:
        rank, suit = hand # The card is a tuple data structure.
        rows[1] += '|{} | '.format(rank.ljust(2))
        rows[2] += '| {} | '.format(suit)
        rows[3] += '|_{}| '.format(rank.rjust(2, '_'))

    for row in rows:
      print(row)


  def calculate_cardvalue(self, card_values):
    """
        Calculates the value of a hand of cards.

        Args:
            cards (list): A list of tuples representing the cards.

        Returns:
            int: The calculated hand value.
    """
    cardnum = 0
    ace_num = False
    for card in card_values:
      if card[0] in ['K', 'Q', 'J']:
        cardnum += 10
      elif card[0] == 'A':
        ace_num += 1
        cardnum += 1
      else:
        cardnum += int(card[0])

    while ace_num > 0 and cardnum < 11:
      cardnum += 10
      ace_num -= 1

    return cardnum

  def choose_move(self, money, cards):
    """
        Prompts the player for their next move.

        Args:
            money (int): The player's available money.
            cards (list): A list of tuples representing the player's cards.

        Returns:
            str: The chosen move (H for Hit, S for Stand, D for Double Down).
    """
    
    moves = ['(H)it', '(S)tand']
    if money>0 and len(cards)==2:
      moves.append('(D)ouble Down')
    while True:
      move = input(f'What you want to do next? {moves} : ').upper()
      if move in ['H', 'S', 'D']:
        return move

  def increase_bet(self, bet_val, money):
    """
    Increases the player's bet amount.

    Args:
        bet_val (int): The current bet amount.
        money (int): The player's available money.

    Returns:
        int: The updated bet amount.
    """
    update_val = self.get_bet()
    self.money = min(bet_val, money)
    bet_val += update_val
    print(f'Update Bet Amount ${bet_val}')
    return bet_val


  def display_cards(self, for_who, _card):
    """
    Displays a player's cards.

    Args:
        player_name (str): The name of the player (Dealer or Player).
        cards (list): A list of tuples representing the player's cards.

    Return:
        _cardnum (int) : provide total card value player of dealer have
    """
    print(f'<---{for_who} Cards--->')
    _cardnum = self.calculate_cardvalue(_card)
    print(f'{for_who} : {_cardnum}')
    self.built_cards(_card, False)
    return _cardnum


  def card_result(self, dealer, player, userbet, money):
    """
    Evaluates the outcome of a round and updates the player's money.

    Args:
        dealer_cards (list): A list of tuples representing the dealer's cards.
        player_cards (list): A list of tuples representing the player's cards.
        bet_amount (int): The player's bet amount.
        money (int): The player's available money.

    Returns:
        tuple: A tuple containing a flag to continue playing and the updated money amount.
    """
    print('\n<--------- RESULT ---------->')
    print(f'\nDEALER: {dealer}   PLAYER: {player}')
    if dealer >= 21:
      print(f'\nDealer busts! Player won ${userbet}!')
      money += userbet
    elif player > 21 or (player < dealer):
      print(f'\nPlayer Lost!!! Dealer won ${userbet}!')
      money -= userbet
    elif player == dealer:
      print(f'\nNeither Player nor Dealer Won\nBet amount ${userbet} is returned back to player')
    elif player > dealer:
      print(f'Player won ${userbet}!')
      money += userbet
    else:
      print(f'\nDealer busts! Player won ${userbet}!')
      money += userbet

    print('\n<--------- RESULT ---------->')

    iscontinue = input('\n\nDo you want to continue the game? [(Y)ES or (N)O] : ').upper()
    return iscontinue, money


  def play_blackjack(self):
      """
          Plays a round of Blackjack.
      """
      money = int(input('\n\nEnter the amount you have for betting? '))

      while money > 0:
          print(f'AMOUNT OF MONEY YOU HAVE FOR BET: {money}')
          card = BlackjackGame(money)
          bet_amount = card.get_bet()

          if bet_amount <= 0:
              break
          print(f'BET AMOUNT : {bet_amount}')
          print('\n\n<---Dealer Cards--->')
          print('DEALER : ???')

          dealer_card = card.draw_cards(2)
          card.built_cards(dealer_card, True)
          player_card = card.draw_cards(2)

          while True:
              player_cardnum = card.display_cards('PLAYER', player_card)

              if player_cardnum > 21:
                  break

              move = card.choose_move(bet_amount, player_card)

              if move == 'D':
                  bet_amount = card.increase_bet(bet_amount, money)

              if move in ['H', 'D']:
                  player_card.extend(card.draw_cards(1))

              if move in ['S', 'D']:
                  player_cardnum = card.display_cards('PLAYER', player_card)
                  break

          dealer_cardnum = card.display_cards('DEALER', dealer_card)

          if player_cardnum <= 21:
            while dealer_cardnum < 17:
                print('\n DEALER HITS NOW....')
                dealer_card.extend(card.draw_cards(1))
                dealer_cardnum = card.display_cards('DEALER', dealer_card)

          isplay, money = card.card_result(dealer_cardnum, player_cardnum, bet_amount, money)

          if isplay != 'Y':
              print('\n\n<----- THANK FOR PLAYING ----->')
              break
      else:
          print(f'\nMONEY YOU HAVE FOR BET: {money}')
          game_over_for_cheaters()







