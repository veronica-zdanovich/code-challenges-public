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
        self.possible_str_len = 0
        self.combinations = list()
        self.digits = None

    def _find_combinations(self, seq: str, digit_index: int):
        if len(seq) >= self.possible_str_len:
            self.combinations.append(seq)
            return seq[:-1]

        for char in self.digit_chars_map[self.digits[digit_index]]:
            seq += char
            digit_index += 1
            seq = self._find_combinations(seq, len(seq))

        return seq[:-1]

    def letterCombinations(self, digits: str) -> List[str]:
        self.possible_str_len = len(digits)
        if self.possible_str_len < 1:
            return self.combinations

        self.digits = digits

        seq = ""
        self._find_combinations(seq, 0)
        return self.combinations
