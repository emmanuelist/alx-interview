#!/usr/bin/python3
import sys
import time  # Importing time module for measuring execution time

"""
    N Queens Problem using Backtracking.

    This modue provides a solution to the N Queens problem using backtracking.
    It takes an integer N as input and prints all possible configurations of
    N queens on an NxN board, suth that no queen attacks another.

    Example:
        >>> python nqueens.py 4
    [(0, 1), (1, 3), (2, 0), (3, 2)]
    [(0, 2), (1, 0), (2, 3), (3, 1)]
    """


def get_solution(board):
    """
    Convert the board configuration into a list of positions.

    Args:
        board (list): A list representing the board configuration, where each
        element is the column index of a queen.

    Returns:
        list: A list of positions, where each position is a tuple of
        (row, column) indices.

    Example:
        >>> board = [1, 3, 0, 2]
        >>> get_solution(board)
        [(0, 1), (1, 3), (2, 0), (3, 2)]
    """
    solution = []
    for i in range(len(board)):
        solution.append([i, board[i]])
    return solution


def is_safe(board, row, col):
    """
    Check if placing a queen at (row, col) is safe.

    Args:
        board (list): A list representing the board configuration,
        where each element is the column index of a queen.
        row (int): The row index to check.
        col (int): The column index to check.

    Returns:
        bool: True if placing a queen at (row, col) is safe, False otherwise.

    Example:
        >>> board = [1, 3, 0, 2]
        >>> is_safe(board, 2, 1)
        False
    """
    for i in range(row):
        # Check if there's a queen in the same column or diagonals
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueens(n, row, board, solutions):
    """
    Recursively solve the N Queens problem using backtracking.

    Args:
        n (int): The size of the board (number of queens).
        row (int): The current row index.
        board (list): A list representing the board configuration, where each
        element is the column index of a queen.
        solutions (list): A list to store all possible solutions.

    Returns:
        None

    Example:
        >>> n = 4
        >>> board = [-1] * n
        >>> solutions = []
        >>> solve_nqueens(n, 0, board, solutions)
        >>> solutions
        [[(0, 1), (1, 3), (2, 0), (3, 2)], [(0, 2), (1, 0), (2, 3), (3, 1)]]
    """
    if row == n:
        # When all queens are placed, add the board configuration to solutions
        solutions.append(get_solution(board))
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col  # Place queen at (row, col)
            # Recur to place next queen
            solve_nqueens(n, row + 1, board, solutions)
            # No need to reset board[row] as it's overwritten i
            # n the next iteration


def main():
    """
    Main function to handle command-line arguments and initiate the solution.

    Args:
        None

    Returns:
        None

    Example:
        >>> python nqueens.py 4
        [(0, 1), (1, 3), (2, 0), (3, 2)]
        [(0, 2), (1, 0), (2, 3), (3, 1)]
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the board with -1 (no queens placed)
    board = [-1] * n
    solutions = []
    solve_nqueens(n, 0, board, solutions)

    # Print all solutions
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
