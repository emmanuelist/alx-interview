# Pascal's Triangle

## Description

This project implements Pascal's Triangle in Python. Pascal's Triangle is a triangular array of numbers where the top row is 1 and each subsequent row contains numbers that are the sum of the two numbers directly above it in the previous row.

## Table of Contents

- [Pascal's Triangle](#pascals-triangle)
  - [Description](#description)
  - [Table of Contents](#table-of-contents)
  - [Requirements](#requirements)
  - [Usage](#usage)
  - [Example](#example)
  - [Flowchart](#flowchart)

## Requirements

- Python 3.6 or higher

## Usage

To use the Pascal's Triangle implementation, you can import the function `pascal_triangle` and call it with the desired number of rows.

```python
from 0-pascal_triangle import pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
```

## Example

```python
guillaume@ubuntu:~/0x00$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

guillaume@ubuntu:~/0x00$ 
guillaume@ubuntu:~/0x00$ ./0-main.py
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
guillaume@ubuntu:~/0x00$ 
```

## Flowchart

Below is a flowchart depicting the logic for generating Pascal's Triangle:

![Pascal's Triangle](https://github.com/emmanuelist/alx-backend-javascript/assets/72014364/15169cba-7b3a-499d-a8bc-252064ff5f52)
