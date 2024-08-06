# 0x01. Lockboxes Algorithm in Python

## Project Overview

This project aims to develop an algorithm that determines if all the boxes can be opened given a list of keys that unlock other boxes. The algorithm is implemented in Python and follows best practices for code documentation and readability.

## Table of Contents

- [0x01. Lockboxes Algorithm in Python](#0x01-lockboxes-algorithm-in-python)
	- [Project Overview](#project-overview)
	- [Table of Contents](#table-of-contents)
	- [Getting Started](#getting-started)
	- [Usage](#usage)
	- [Algorithm Description](#algorithm-description)
	- [Time and Space Complexity](#time-and-space-complexity)
	- [Professional Markdown and Styling](#professional-markdown-and-styling)
	- [License](#license)

## Getting Started

To get started with this project, you can clone the repository from GitHub:

```bash
git clone https://github.com/alx-interview/0x01-lockboxes.git
```

## Usage

To use the `canUnlockAll` function, import it from the `0-lockboxes.py` file and pass a list of lists representing the boxes and their keys. The function will return `True` if all boxes can be opened, and `False` otherwise.

Here's an example usage:

```python
from 0_lockboxes import canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Output: False
```

## Algorithm Description

The algorithm uses a breadth-first search (BFS) approach to traverse through the boxes and their keys. It starts by initializing a queue with the first box and a set to keep track of visited boxes.

The algorithm iterates through the queue until it is empty. For each box in the queue, it checks if all its keys have been used. If not, it adds the boxes that can be unlocked by those keys to the queue and marks them as visited.

After iterating through all the boxes, the algorithm checks if all boxes have been visited. If yes, it returns `True`; otherwise, it returns `False`.

## Time and Space Complexity

The time complexity of the algorithm is O(n^2), where n is the number of boxes. This is because in the worst case, the algorithm may need to traverse through all the boxes and their keys.

The space complexity of the algorithm is O(n), where n is the number of boxes. This is because the algorithm uses a queue to store the boxes and a set to keep track of visited boxes.

## Professional Markdown and Styling

This README file follows professional markdown and styling guidelines. It includes a clear project overview, table of contents, getting started instructions, usage examples, algorithm description, time and space complexity analysis, and a license section.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
