import random, datetime

class BirthdayParadox():

  def __init__(self, total_birthday, year):
    """
    Initializes the BirthdayParadox class with the given parameters.

    Args:
    total_birthday (int): The total number of birthdays to generate.
    year (datetime.date): The year for which birthdays will be generated.
    """
    self.total_birthday = total_birthday
    self.year = year

  def generate_birthdays(self):
    """
    Generates a list of random birthdates for the specified year.

    Returns:
    list: A list containing randomly generated birthdates.
    """
    birthdays = []
    for i in range(self.total_birthday):
      day = datetime.timedelta(random.randint(0, 365))
      birthdate = year + day
      birthdays.append(birthdate)
    return birthdays
    

  def match_birthdays(self, birthdays):
    """
    Checks if there are any matching birthdays in the given list.

    Args:
    birthdays (list): A list of birthdates to check for matches.

    Returns:
    int: Returns 1 if at least one pair of matching birthdays is found, -1 otherwise.
    """
    if len(birthdays) == len(set(birthdays)):
      return -1
    else:
      is_birthdate_present = set()
      for birth in birthdays:
        if birth in is_birthdate_present:
          return 1
        is_birthdate_present.add(birth)
    
  def calculate_probs(self):
    """
    Runs simulations to calculate the probability of the birthday paradox.

    Returns:
    int: The number of simulations where at least one pair of matching birthdays was found.
    """
    same_birthday = 0
    for i in range(100_000):

      if i%10_000 == 0:
        print(f'Running Simulation : {i}\n')

      birthdays = self.generate_birthdays()
      similar_birthdays = self.match_birthdays(birthdays)

      if similar_birthdays != -1 :
        same_birthday += 1

    return same_birthday


if __name__ == "__main__":
  while True:
    total_birthday = int(input('How many bithdays do you want? (1-100) '))
    if not 1 < total_birthday < 100 :
      print('number of birthdays should not be greater than 100')
    else:
      break

  while True:
    required_year = int(input('In which year do you want to simulate the birthday paradox: '))
    if not required_year >= 1:
      print('Enter Valid Year\n')
    else:
      break

  year = datetime.date(required_year, 1, 1)
  birthdate = BirthdayParadox(total_birthday, year)
  prob = birthdate.calculate_probs()
  print('Out of 100,000 simulations of', total_birthday, 'people, there was a')
  print('matching birthday in that group', prob, 'times. This means')
  print('that', total_birthday, 'people have a', round((prob/100_000)*100, 2), '% chance of')
  print('having a matching birthday in their group.')
  print('That\'s probably more than you would think!')




