class Solution:
    def __init__(self):
        self.cache = dict()

    def get_min_distance(self, word1: str, word2: str, word1_index: int, word2_index: int):
        if self.cache.get((word1_index, word2_index)) is not None:
            return self.cache[(word1_index, word2_index)]

        if word1_index == 0 and word2_index == 0:
            return 0

        if word1_index == 0 and word2_index > 0:
            return word2_index

        if word2_index == 0 and word1_index > 0:
            return word1_index

        is_equal = word1[word1_index - 1] == word2[word2_index - 1]
        diff = 0 if is_equal else 1

        without_two_chars = self.get_min_distance(word1, word2, word1_index - 1, word2_index - 1) + diff
        without_word1_char = self.get_min_distance(word1, word2, word1_index - 1, word2_index) + 1
        without_word2_char = self.get_min_distance(word1, word2, word1_index, word2_index - 1) + 1

        self.cache[(word1_index, word2_index)] = min(without_word1_char, without_word2_char, without_two_chars)
        return min(without_word1_char, without_word2_char, without_two_chars)

    def minDistance(self, word1: str, word2: str) -> int:
        word1_index = len(word1)
        word2_index = len(word2)
        return self.get_min_distance(word1, word2, word1_index, word2_index)
