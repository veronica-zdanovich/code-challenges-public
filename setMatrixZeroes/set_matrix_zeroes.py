from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        first_row_contains_zero = False
        first_col_contains_zero = False

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i == 0:
                        first_row_contains_zero = True
                    if j == 0:
                        first_col_contains_zero = True

                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_row_contains_zero:
            for y in range(n):
                matrix[0][y] = 0
        if first_col_contains_zero:
            for x in range(m):
                matrix[x][0] = 0

