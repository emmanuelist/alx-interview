# N Queens Problem

## Project Overview

The **N Queens** problem is a classic algorithmic challenge in computer science and mathematics. The goal is to place N non-attacking queens on an N×N chessboard. A solution requires that no two queens share the same row, column, or diagonal. This problem demonstrates the application of backtracking algorithms and is a fundamental example of recursive problem-solving.

This project involves writing a Python program to solve the N Queens problem, with a specific focus on algorithmic thinking and optimization.

## Concepts and Requirements

### Key Concepts

To successfully complete the project, a solid understanding of the following concepts is essential:

1. **Backtracking Algorithms**:
   - Backtracking is an algorithmic technique for solving problems incrementally. It involves exploring potential solutions, and discarding them if they are not viable.
   - [Backtracking Introduction](https://en.wikipedia.org/wiki/Backtracking)

2. **Recursion**:
   - Recursion is the process of defining a function in terms of itself. It is a powerful tool for implementing backtracking algorithms.
   - [Recursion in Python](https://realpython.com/python-recursion/)

3. **List Manipulations in Python**:
   - Lists are used to store the positions of queens on the board. Efficient list manipulation is crucial for tracking and updating these positions.
   - [Python Lists](https://docs.python.org/3/tutorial/datastructures.html)

4. **Python Command-Line Arguments**:
   - The program will take the size of the board (N) as a command-line argument.
   - [Command Line Arguments in Python](https://docs.python.org/3/howto/argparse.html)

### General Requirements

- **Editors**: Allowed editors include `vi`, `vim`, and `emacs`.
- **Operating System**: The program will be tested on Ubuntu 20.04 LTS using Python 3 (version 3.4.3).
- **File Format**:
  - All files should end with a new line.
  - The first line of all files should be `#!/usr/bin/python3`.
- **README**: A `README.md` file at the root of the project folder is mandatory.
- **Code Style**: The code must adhere to PEP 8 style guidelines (version 1.7.*).
- **Execution**: All files must be executable.

## Task Description

### Task 0: N Queens

**Objective**: Write a Python program that solves the N Queens problem.

- **Usage**: `nqueens N`
  - The program should be called with one argument: `N`, the size of the chessboard (N x N).
- **Input Validation**:
  - If the user provides the wrong number of arguments, print `Usage: nqueens N`, followed by a new line, and exit with status code `1`.
  - If `N` is not an integer, print `N must be a number`, followed by a new line, and exit with status code `1`.
  - If `N` is less than 4, print `N must be at least 4`, followed by a new line, and exit with status code `1`.
- **Output**:
  - The program should print every possible solution to the problem, one solution per line.
  - Each solution should be in the format of a list of lists, where each inner list represents the position of a queen on the board in the form `[row, column]`.

**Example**:

```bash
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]

$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```

### File Structure

- **`0-nqueens.py`**: The main Python script that implements the solution to the N Queens problem.

### Repository Structure

- **GitHub Repository**: `alx-interview`
- **Project Directory**: `0x05-nqueens`
- **Primary File**: `0-nqueens.py`

## Additional Resources

- **Mock Interview**: Practice and refine your understanding of backtracking and recursion by solving similar problems.

## Conclusion

The **N Queens** project is not just about solving a well-known problem but is also a means to enhance your understanding of recursive algorithms and their applications. By completing this project, you will develop a deeper appreciation for algorithmic problem-solving, which is a crucial skill in the field of computer science.