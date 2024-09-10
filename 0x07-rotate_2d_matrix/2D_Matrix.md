### Diagram Explanation

1. **Initial Matrix**: The starting point is the original n x n matrix.
2. **Transpose the Matrix**: Swap rows with columns, effectively turning the matrix on its side without changing the order of elements in each row.
3. **Reverse Each Row**: After transposing, reverse each row to achieve the final 90-degree clockwise rotation.

### Step-by-Step Diagram

```
**Step 1: Initial Matrix**

Matrix:

[ 1  2  3 ]
[ 4  5  6 ]
[ 7  8  9 ]

**Step 2: Transpose the Matrix**

Transpose:

[ 1  4  7 ]
[ 2  5  8 ]
[ 3  6  9 ]

Explanation: Swap elements at (i, j) with (j, i).

**Step 3: Reverse Each Row**

Final Rotated Matrix:

[ 7  4  1 ]
[ 8  5  2 ]
[ 9  6  3 ]

Explanation: Reverse each row to achieve the 90-degree clockwise rotation.
```

### Detailed Breakdown

1. **Transposition**:

   - Swap elements along the diagonal. For example, swap (0,1) with (1,0), (0,2) with (2,0), and so on.

   Transposing `[1, 2, 3]` and `[4, 5, 6]` results in:

   - `1` stays in place.
   - `2` swaps with `4`.
   - `3` swaps with `7`.
   - Continue this for all elements above the diagonal.

2. **Reversing Rows**:
   - Reverse each row of the transposed matrix.
   - `[1, 4, 7]` becomes `[7, 4, 1]`.
   - `[2, 5, 8]` becomes `[8, 5, 2]`.
   - `[3, 6, 9]` becomes `[9, 6, 3]`.

This step-by-step transformation shows how the in-place matrix rotation is accomplished efficiently without needing extra space, adhering to the problem constraints.

![2D_matrix](https://github.com/user-attachments/assets/14342606-3990-4224-b079-876bd771b74d)
