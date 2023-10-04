# Birthday Paradox Simulation
This Python script simulates the Birthday Paradox, a famous probability problem. It calculates the probability of at least two people sharing the same birthday among a given number of randomly selected birthdays.

## Introduction
The Birthday Paradox is a phenomenon where it is more likely than you might expect that two or more people in a group will share the same birthday. This script helps you understand and visualize this probability by running simulations.

## Usage
1. Clone the repository or download the script.

2. Ensure you have Python 3 installed.

3. Run the script using a Python interpreter:

      python birthday_paradox.py

Follow the prompts to input the total number of birthdays you want to simulate and the year for the simulation.

## How it Works
1. The script generates random birthdays for the specified number of people.
2. It checks if there are any matching birthdays.
3. The simulation is repeated 100,000 times to estimate the probability.

## Sample Output
Here is an example of what the script output might look like:

      How many bithdays do you want? (1-100) : 50
      In which year do you want to simulate the birthday paradox (e.g., 2023): 2023

      Running Simulation: 0
      Running Simulation: 10000
      Running Simulation: 20000
      Running Simulation: 30000
      Running Simulation: 40000
      Running Simulation: 50000
      Running Simulation: 60000
      Running Simulation: 70000
      Running Simulation: 80000
      Running Simulation: 90000

## Result:
Out of 100,000 simulations, 62,847 had at least two people sharing the same birthday.

      Probability of a shared birthday: 62.85%
This output demonstrates the estimated probability of the Birthday Paradox for the specified input.

Feel free to modify the script and adapt it to your needs.

Happy exploring the Birthday Paradox!