# Coin Change Problem

## Overview

The Coin Change problem is a classic algorithmic challenge where you are given a set of coin denominations and a total amount. The objective is to find the minimum number of coins needed to make up the given total amount. This problem can be approached using different techniques, including greedy algorithms and dynamic programming.

## Concepts Covered

### 1. Greedy Algorithms

- **Definition**: Greedy algorithms make locally optimal choices at each step with the hope of finding a global optimum.
- **Application**: While greedy algorithms can be efficient, they don't always provide the optimal solution for the coin change problem, especially when the coin denominations do not fit certain patterns.

### 2. Dynamic Programming (DP)

- **Definition**: Dynamic programming is a method for solving complex problems by breaking them down into simpler sub-problems, storing the results of sub-problems to avoid redundant work.
- **Key Concepts**:
  - **Overlapping Subproblems**: The problem can be broken into subproblems that are reused several times.
  - **Optimal Substructure**: An optimal solution to the problem can be constructed from optimal solutions to its subproblems.

### 3. Algorithmic Complexity

- **Time Complexity**: The amount of time an algorithm takes to complete as a function of the size of the input.
- **Space Complexity**: The amount of memory space an algorithm uses as a function of the size of the input.

## Problem Statement

You are given a pile of coins with different values. Determine the fewest number of coins needed to make up a given amount `total`.

### Function Prototype

```python
def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.

    Parameters:
    coins (list of int): The values of the coins available.
    total (int): The total amount to make up.

    Returns:
    int: The minimum number of coins needed to make up the total amount,
         or -1 if it is not possible.
    """
```

### Requirements

- If `total` is 0 or less, return 0.
- If `total` cannot be met by any number of coins you have, return -1.
- Assume you have an infinite number of each denomination of coin in the list.

## Setup and Usage

### Prerequisites

- Python 3.4.3 or higher

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/alx-interview.git
   ```

2. Navigate to the project directory:

   ```bash
   cd alx-interview/0x08-making_change
   ```

### Running the Code

Ensure the main file and the module are executable:

```bash
chmod +x 0-main.py 0-making_change.py
```

Run the main file:

```bash
./0-main.py
```

### Example

```python
# Example usage
print(makeChange([1, 2, 25], 37))  # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
```

## Algorithmic Approach

### Greedy Algorithm (Approach 1)

- **Strategy**: Always pick the largest denomination coin that does not exceed the remaining amount.
- **Limitation**: May not always yield the optimal solution.

### Dynamic Programming Approach

- **Strategy**: Use a table to store the minimum number of coins needed for all amounts up to the given total.
- **Implementation**:
  - Initialize a table `dp` where `dp[i]` represents the minimum number of coins needed for amount `i`.
  - Set `dp[0] = 0` (base case).
  - For each coin and each amount, update the `dp` table to reflect the minimum number of coins needed.

## Complexity Analysis

### Greedy Algorithm

- **Time Complexity**: O(n) where n is the number of coins.
- **Space Complexity**: O(1)

### Dynamic Programming

- **Time Complexity**: O(n \* m) where n is the total amount and m is the number of coins.
- **Space Complexity**: O(n)

## Resources

- **[Python Official Documentation](https://docs.python.org/3/tutorial/controlflow.html)**: Control flow tools including loops and conditional statements.
- **[GeeksforGeeks - Coin Change | DP-7](https://www.geeksforgeeks.org/coin-change-dp-7/)**: In-depth explanation of the dynamic programming approach to the coin change problem.
- **[GeeksforGeeks - Greedy Algorithm to find Minimum number of Coins](https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/)**: Explanation of the greedy algorithm approach.
- **[YouTube - Dynamic Programming - Coin Change Problem](https://www.youtube.com/watch?v=1R0_7HqNaW0)**: A visual and step-by-step explanation of the dynamic programming approach.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to [ALX](https://www.alxafrica.com/) for providing this challenge and the resources to tackle it.

---

This README covers the necessary aspects of the project, including the problem statement, algorithmic approaches, implementation details, and usage instructions. Remember to replace placeholder text with actual data and links where needed.
