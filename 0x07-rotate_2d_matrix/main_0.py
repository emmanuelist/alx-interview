#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix with Execution Time Measurement
"""
import time
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    # Define a sample 3x3 matrix
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    
    # Measure start time
    start_time = time.time()
    
    # Rotate the matrix
    rotate_2d_matrix(matrix)
    
    # Measure end time
    end_time = time.time()
    
    # Print the rotated matrix
    print(matrix)
    
    # Print the execution time
    print(f"Execution time: {end_time - start_time:.10f} seconds")
