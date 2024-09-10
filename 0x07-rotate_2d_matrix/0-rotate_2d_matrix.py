#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90 degrees clockwise in place.

    :param matrix: List of lists where each sublist represents
    a row of the matrix.
    """
    # Transpose the matrix (swap rows and columns)
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row to complete the 90-degree clockwise rotation
    for i in range(n):
        matrix[i].reverse()
