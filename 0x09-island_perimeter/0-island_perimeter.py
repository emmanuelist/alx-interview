#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island represented by a grid of 0s and 1s.

    The grid is a 2D list where each cell
    contains either 0 (water) or 1 (land).
    The island is formed by connecting
    adjacent lands horizontally or vertically.

    Parameters:
    grid (List[List[int]]): A 2D list representing the island.
    Each cell contains 0 or 1.

    Returns:
    int: The perimeter of the island. The perimeter is the total length of the
    boundaries of the island.
    """
    area = 0
    for row in grid + list(map(list, zip(*grid))):
        for i1, i2 in zip([0] + row, row + [0]):
            area += int(i1 != i2)
    return area
