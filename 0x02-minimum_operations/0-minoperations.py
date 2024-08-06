#!/usr/bin/python3
""" Module for 0-minoperations"""


def minOperations(n):
    """
    minOperations
    Gets fewest # of operations needed to result in exactly n H characters
    """
    # If n is less than 2, no operations are needed
    if (n < 2):
        return 0

    # Initialize the number of operations and the factor to start checking from
    ops, root = 0, 2

    # Loop until root exceeds n
    while root <= n:
        # If n is evenly divisible by root
        if n % root == 0:
            # Add the factor to the operations count
            ops += root
            # Divide n by the factor
            n = n / root
            # Decrement root to check for smaller factors
            root -= 1
        # Increment root to check the next potential factor
        root += 1

    return ops
