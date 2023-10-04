import random

class DeductiveLogicGame():

  def __init__(self, max_guess):
    """
    Initializes the DeductiveLogicGame class with the given maximum number of guesses.

    Args:
    max_guess (int): The maximum number of guesses allowed in the game.
    """
    self.max_guess = max_guess

  def guess_num(self):
    """
    Starts the game and allows the user to guess the secret number within a limited number of attempts.
    """
    play = True
    while play:
      secret_num = str(random.randint(100, 1000))
      curr_guess = 1
      while curr_guess <= self.max_guess:
        user_guess = input(f'Guess no. {curr_guess} : ')
        if len(user_guess) < 3:
          print('\nEnter three digit number')

        is_guess = self.clues(user_guess, secret_num)
        
        if is_guess == 'True':
          print('You got it!')
          isplay = input('Do you want to play again? yes/no : ')
          break
        print(f'{is_guess}\n')
        curr_guess += 1

      if curr_guess > self.max_guess:
        print(f'Your are out of guess \nSecret Numer : {secret_num}\n')
        isplay = input('Do you want to play again? yes/no : \n')

      play = False if isplay == 'no' else True

  def clues(self, user_guess, secret_num):
    """
    Provides clues based on the user's guess and the secret number.

    Args:
    user_guess (str): The user's guess as a string.
    secret_num (str): The secret number as a string.

    Returns:
    str: A clue that indicates the similarity between the user's guess and the secret number.
    """
    for idx, num in enumerate(user_guess):
      if user_guess == secret_num:
        return 'True'
      elif user_guess[idx] == secret_num[idx]:
        return 'FERMI'
      elif num in secret_num:
        return 'PICO'
      else:
        continue
    return 'BAGELS'


if __name__ == "__main__":
  max_guess = 10
  print(f'I have chosen a 3-digit number. See if you can guess it! I will give you hints: \n\nWhen I say "Pico", it means one digit is correct but in the wrong position.\nWhen I say "Fermi", it means one digit is correct and in the right position.\nIf I say "Bagels", none of the digits are correct.\n\nI have got the number in mind, and you have {max_guess} attempts to figure it out.\n\n')
  game = DeductiveLogicGame(max_guess)
  result = game.guess_num()