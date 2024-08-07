#!/usr/bin/python3
"""
Prime Game Module

This module provides functions to play a prime number game between Maria and Ben.
"""

def is_winner(x: int, nums: list) -> str:
    """
    Determines the winner of the prime game.

    Args:
        x (int): The number of rounds.
        nums (list): A list of numbers.

    Returns:
        str: The winner of the game, either "Ben" or "Maria". If it's a tie, returns None.

    Raises:
        ValueError: If x is less than or equal to 0, or if nums is None, or if x is not equal to the length of nums.
    """
    if x <= 0:
        raise ValueError("x must be greater than 0")
    if nums is None:
        raise ValueError("nums cannot be None")
    if x != len(nums):
        raise ValueError("x must be equal to the length of nums")

    ben = 0
    maria = 0

    max_num = max(nums)
    a = [1] * (max_num + 1)
    a[0] = a[1] = 0

    for i in range(2, len(a)):
        rm_multiples(a, i)

    for i in nums:
        if sum(a[:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1

    if ben > maria:
        return "Ben"
    elif maria > ben:
        return "Maria"
    else:
        return None


def rm_multiples(ls: list, x: int) -> None:
    """
    Removes multiples of primes from the list.

    Args:
        ls (list): The list to modify.
        x (int): The prime number.

    Returns:
        None
    """
    for i in range(x, len(ls), x):
        ls[i] = 0
