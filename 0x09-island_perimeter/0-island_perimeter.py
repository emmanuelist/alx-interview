#!/usr/bin/python3
"""0. Prime Game - Maria and Ben are playing a game"""


def isWinner(x, nums):
    """
    Determine the winner of the prime game between Maria and Ben.

    The game is played in x rounds, and in each round, a number from the list nums is chosen.
    A player wins a round if the sum of all prime numbers up to the chosen number is even.
    The player who wins the most rounds wins the game.

    Args:
        x (int): The number of rounds.
        nums (list): A list of numbers.

    Returns:
        str: The winner of the game, either "Ben" or "Maria". If the game is a tie, returns None.
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    ben = 0
    maria = 0

    a = [1 for x in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0
    for i in range(2, len(a)):
        rm_multiples(a, i)

    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def rm_multiples(ls, x):
    """
    Remove multiples of a prime number from a list.

    Args:
        ls (list): The list to modify.
        x (int): The prime number.

    Returns:
        None
    """
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
