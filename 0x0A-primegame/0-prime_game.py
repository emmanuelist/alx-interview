#!/usr/bin/python3


def findMultiples(num, targets):
    """
    Remove multiples of `num` from the `targets` list.

    Args:
        num (int): The number to find multiples of.
        targets (list): The list of numbers to remove multiples from.

    Returns:
        list: The updated list with multiples of `num` removed.

    Example:
        >>> findMultiples(3, [1, 2, 3, 4, 5, 6])
        [1, 2, 4, 5]
    """

    for i in targets:
        if i % num == 0:
            targets.remove(i)
    return targets


def isPrime(i):
    """
    Check if `i` is a prime number.

    Args:
        i (int): The number to check.

    Returns:
        bool: True if `i` is prime, False otherwise.

    Example:
        >>> isPrime(5)
        True
        >>> isPrime(6)
        False
    """
    if i == 1:
        return False
    for j in range(2, i):
        if i % j == 0:
            return False
    return True


def findPrimes(n):
    """
    Find the number of prime numbers in the range [1, `n`].

    Args:
        n (int): The upper bound of the range.

    Returns:
        int: The number of prime numbers in the range.

    Example:
        >>> findPrimes(10)
        4
    """

    counter = 0
    target = list(n)
    for i in range(1, len(target) + 1):
        if isPrime(i):
            counter += 1
            target.remove(i)
            target = findMultiples(i, target)
        else:
            pass
    return counter


def isWinner(x, nums):
    """
    Determine the winner of a game based on the number of prime
    numbers in each round.

    Args:
        x (int): The number of rounds.
        nums (list): The list of numbers for each round.

    Returns:
        str: The winner of the game ('Maria' or 'Ben') or None if it's a tie.

    Example:
        >>> isWinner(3, [4, 5, 6])
        'Maria'
    """

    players = {'Maria': 0, 'Ben': 0}
    cluster = set()
    for elem in range(x):
        nums.sort()
        num = nums[elem]
        for i in range(1, num + 1):
            cluster.add(i)
            if i == num + 1:
                break
        temp = findPrimes(cluster)

        if temp % 2 == 0:
            players['Ben'] += 1
        elif temp % 2 != 0:
            players['Maria'] += 1

    if players['Maria'] > players['Ben']:
        return 'Maria'
    elif players['Maria'] < players['Ben']:
        return 'Ben'
    else:
        return None
