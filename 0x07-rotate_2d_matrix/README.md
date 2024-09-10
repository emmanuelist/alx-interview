# 0x07. Rotate 2D Matrix

This project involves implementing an in-place algorithm to rotate an n x n 2D matrix by 90 degrees clockwise using Python. It is part of the ALX interview preparation series and focuses on matrix manipulation, in-place operations, and algorithmic thinking.

## Learning Objectives

- Understand how to represent and manipulate 2D matrices using lists of lists in Python.
- Perform in-place operations to optimize space complexity.
- Comprehend matrix transposition and how it contributes to the rotation process.
- Apply nested loops to modify matrix elements effectively.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- Files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.8.10).
- Files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/python3`.
- Include a `README.md` file at the root of the project folder.
- Code should conform to `pycodestyle` (version 2.8.0).
- You are not allowed to import any external modules.
- All modules and functions must be documented.
- Files must be executable.

## Task

### 0. Rotate 2D Matrix (Mandatory)

Given an n x n 2D matrix, rotate it 90 degrees clockwise in place.

**Prototype:**

```python
def rotate_2d_matrix(matrix):
```

- The function does not return anything; it modifies the matrix in place.
- The matrix is assumed to have two dimensions and will not be empty.

### Example

```python
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
```

**Output:**

```
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```

## Key Concepts and Resources

- **Matrix Representation in Python**: Learn how to work with 2D matrices using lists of lists.
- **In-place Operations**: Understand how to modify matrices without creating additional copies.
- **Matrix Transposition**: Grasp the concept of swapping rows and columns to prepare the matrix for rotation.
- **Reversing Rows**: Reverse each row to complete the 90-degree rotation.
- **Nested Loops**: Use nested loops effectively to access and manipulate matrix elements.

### Resources

- [Python Official Documentation](https://docs.python.org/3/tutorial/datastructures.html)
- [In-place Rotate Square Matrix by 90 degrees (GeeksforGeeks)](https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/)
- [Transpose a Matrix in Python (GeeksforGeeks)](https://www.geeksforgeeks.org/transpose-matrix-single-line-python/)
- [Python Lists (TutorialsPoint)](https://www.tutorialspoint.com/python/python_lists.htm)

## Getting Started

### Prerequisites

Ensure you have Python 3.8.10 installed and that your environment meets the project requirements.

### Running the Tests

1. Create the file `0-rotate_2d_matrix.py` and implement the `rotate_2d_matrix` function.
2. Create a test file (e.g., `main_0.py`) and test your implementation using sample matrices.
3. Run the test script to verify your function:

   ```bash
   ./main_0.py
   ```

## Project Structure

```plaintext
.
├── 0-rotate_2d_matrix.py  # Contains the implementation of the rotate_2d_matrix function
├── main_0.py              # Test script for the function
└── README.md              # This file
```

## Author

- **Emmanuel Paul.** - [GitHub](https://github.com/emmanuelist)

## License

This project is part of the ALX Software Engineering curriculum and is intended for educational purposes.
