from typing import List


class Solution:
    def __init__(self):
        self.digit_chars_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        self.possible_len = 0
        self.combinations = list()
        self.max_letters_len = 4

    def combine(self, seq: str, digit_index: int, digits: str) -> str:
        if len(seq) == self.possible_len:
            self.combinations.append(seq)
            return ""

        for char in self.digit_chars_map[digits[digit_index]]:
            seq += char
            self.combine(seq, digit_index + 1, digits)
            seq = seq[:-1]

    def letterCombinations(self, digits: str) -> List[str]:
        self.possible_len = len(digits)
        if len(digits) < 1:
            return self.combinations
        seq = ""
        self.combine(seq, 0, digits)
        return self.combinations
