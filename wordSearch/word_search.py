from typing import List


class Solution:
    def dfs(self, board: List[List[str]], word: str, i: int, j: int, word_index: int):
        if word_index == len(word):
            return True

        if i >= len(board) or i < 0:
            return False

        if j >= len(board[0]) or j < 0:
            return False

        if board[i][j] != word[word_index]:
            return False

        char = board[i][j]
        board[i][j] = ""

        top = self.dfs(board, word, i - 1, j, word_index + 1)
        bottom = self.dfs(board, word, i + 1, j, word_index + 1)
        left = self.dfs(board, word, i, j - 1, word_index + 1)
        right = self.dfs(board, word, i, j + 1, word_index + 1)

        found = top or bottom or left or right
        if found:
            return True

        board[i][j] = char
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, i, j, 0):
                    return True
        return False
