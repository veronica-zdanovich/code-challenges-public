class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        max_row = len(word1) + 1
        max_col = len(word2) + 1
        matrix = [0 for _ in range(max_row * max_col)]

        for row in range(0, max_row):
            matrix[row * max_col] = row

        for col in range(0, max_col):
            matrix[col] = col

        for row in range(1, max_row):
            current_row = row * max_col
            prev_row = (row - 1) * max_col
            for col in range(1, max_col):
                diff = word1[row - 1] != word2[col - 1]
                prev_i = matrix[prev_row + col] + 1
                prev_j = matrix[current_row + col - 1] + 1
                prev_diag = matrix[prev_row + col - 1] + diff

                matrix[current_row + col] = min(prev_i, prev_j, prev_diag)

        return matrix[max_row * max_col - 1]
