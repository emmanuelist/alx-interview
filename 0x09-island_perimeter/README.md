# Island Perimeter Algorithm in Python

## Description

This repository contains a Python function that calculates the perimeter of an island represented by a grid of 0s and 1s. The grid is a 2D list where each cell contains either 0 (water) or 1 (land). The island is formed by connecting adjacent lands horizontally or vertically.

## Function

The function `island_perimeter(grid)` takes a 2D list representing the island as a parameter and returns the perimeter of the island. The perimeter is the total length of the boundaries of the island.

## Usage

To use the function, import it from the `0-island_perimeter.py` file and call the function with a 2D list representing the island.

Here's an example:

```python
island_perimeter = __import__('0-island_perimeter').island_perimeter

grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

print(island_perimeter(grid))  # Output: 12
```

## Algorithm

The algorithm used in this function is as follows:

1. Initialize a variable `area` to 0.
2. Iterate over the grid and its transpose (obtained by swapping rows and columns) using nested loops.
3. For each cell in the combined grid, check if it is a land cell (1) by comparing it with the adjacent cells (horizontally and vertically).
4. If the current cell is a land cell and its adjacent cell is either a water cell (0) or out of bounds, increment the `area` by 1.
5. Return the final value of `area` as the perimeter of the island.

## Resources

- [Python Official Documentation: Nested Lists](https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions)
- [GeeksforGeeks: Python Multi-dimensional Arrays](https://www.geeksforgeeks.org/python-multi-dimensional-arrays/)
- [TutorialsPoint: Python Lists](https://www.tutorialspoint.com/python/python_lists.htm)
- [YouTube Tutorials: Python 2D arrays and lists](https://www.youtube.com/watch?v=Cgz7DqDLjQU)

## Author

[Emmanuel Paul](https://github.com/emmauelist)

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Acknowledgments

- [Alx Interview](https://github.com/alx-interview) for providing the initial problem and the evaluation criteria.
- [Python](https://www.python.org/) for being an excellent programming language for this task.
- [PEP 8](https://www.python.org/dev/peps/pep-0008/) for providing a style guide for Python code.
