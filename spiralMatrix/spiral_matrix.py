from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral_list = list()
        m = len(matrix)
        n = len(matrix[0])

        start_pointer_m, start_pointer_n = 0, 0
        end_pointer_m, end_pointer_n = m - 1, n - 1
        while len(spiral_list) < m * n:
            spiral_list += [matrix[start_pointer_m][j] for j in range(start_pointer_n, end_pointer_n + 1)]
            if end_pointer_n - start_pointer_n < 0:
                break
            start_pointer_m += 1

            spiral_list += [matrix[i][end_pointer_n] for i in range(start_pointer_m, end_pointer_m + 1)]
            if end_pointer_m - start_pointer_m < 0:
                break
            end_pointer_n -= 1

            spiral_list += [matrix[end_pointer_m][j] for j in range(end_pointer_n, start_pointer_n - 1, -1)]
            if end_pointer_n - start_pointer_n < 0:
                break
            end_pointer_m -= 1

            spiral_list += [matrix[i][start_pointer_n] for i in range(end_pointer_m, start_pointer_m - 1, -1)]
            if end_pointer_m - start_pointer_m < 0:
                break
            start_pointer_n += 1

        return spiral_list
