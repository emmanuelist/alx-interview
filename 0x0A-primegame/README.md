# 0x0A-Prime Game: A Competitive Game of Prime Numbers

## Introduction

Welcome to the 0x0A-Prime Game, a challenging programming project that requires an understanding of prime numbers, game theory, and algorithm optimization. In this game, two players, Maria and Ben, take turns selecting prime numbers from a set of consecutive integers and removing them along with their multiples from the set. The player who cannot make a move loses the game.

The goal of this project is to determine the winner of each round based on the strategic removal of prime numbers and their multiples. The winner is determined by the player who wins the most rounds.

## Requirements

- The game will be played for `x` rounds, where `x` is not larger than 10000.
- Each round will have a different upper limit `n`.
- Maria always goes first and both players play optimally.
- If the winner cannot be determined, the result for that round will be `None`.

## Installation

To run the code, you will need to have Python 3 installed on your system. You can download Python 3 from the official website: https://www.python.org/downloads/

Once Python 3 is installed, you can clone the repository from GitHub:

```bash
git clone https://github.com/emmanuelist/alx-interview.git
```

Navigate to the project directory:

```bash
cd alx-interview/0x0A-primegame
```

## Usage

To determine the winner of each round, you can use the `isWinner` function provided in the `0-prime_game.py` file. The function takes two arguments: `x` (the number of rounds) and `nums` (an array of `n` values for each round).

Here's an example usage:

```python
from 0_prime_game import isWinner

x = 3
nums = [4, 5, 1]

winner = isWinner(x, nums)
print("Winner: {}".format(winner))
```

Output:

```
Winner: Ben
```

## Code Structure

The code is organized into a single Python file, `0-prime_game.py`, which contains the following functions:

1. `findMultiples(num, targets)`: This function removes multiples of `num` from the `targets` list.

2. `isPrime(i)`: This function checks if `i` is a prime number.

3. `findPrimes(n)`: This function finds the number of prime numbers in the range [1, `n`].

4. `isWinner(x, nums)`: This function determines the winner of each round based on the number of prime numbers in each round.

## Resources

To help you understand the concepts and implement the solution, you can refer to the following resources:

- Prime Numbers:

  - Khan Academy: Prime Numbers: Introduction to prime numbers (https://www.khanacademy.org/math/number-theory/prime-numbers)

- Sieve of Eratosthenes:

  - Sieve of Eratosthenes in Python: A step-by-step guide to implementing the sieve algorithm in Python (https://www.geeksforgeeks.org/sieve-of-eratosthenes/)

- Game Theory:

  - Game Theory Introduction: A simple explanation of game theory and strategic decision-making (https://www.youtube.com/watch?v=h_tpT4i90r0)

- Dynamic Programming/Memoization:

  - Dynamic Programming: What Is Dynamic Programming With Python Examples (https://www.geeksforgeeks.org/dynamic-programming/)

- Python Programming:
  - Python Lists: Managing lists in Python (https://www.w3schools.com/python/python_lists.asp)

This project was created by E for the ALX Interview Preparation Program.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

## Acknowledgments

I would like to thank ALX for their guidance and support throughout the project.

## Contact

If you have any questions or need further assistance, please feel free to contact me at emmanuel.paul75@yahoo.com.
