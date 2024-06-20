from collections import defaultdict
from typing import List


class Solution:
    def __init__(self):
        self.key = 0

    def _char_to_int(self, char: str) -> int:
        match char:
            case "A":
                return 0
            case "C":
                return 1
            case "G":
                return 2
            case "T":
                return 3

    def _int_to_char(self, num: int) -> str:
        match num:
            case 0:
                return "A"
            case 1:
                return "C"
            case 2:
                return "G"
            case 3:
                return "T"

    def _update_key(self, new_char: str):
        self.key = (self.key << 2 & 0xFFFFF) | self._char_to_int(new_char)

    def _convert_to_str(self, key: int) -> str:
        string = ""
        while len(string) != 10:
            string = self._int_to_char(key & 0x3) + string
            key = key >> 2
        return string

    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequences_dict = defaultdict(int)
        if len(s) < 10:
            return []

        for i in range(10):
            self._update_key(s[i])
        sequences_dict[self.key] = 1

        for index in range(1, len(s) - 9):
            self._update_key(s[index + 9])
            sequences_dict[self.key] += 1
        return [self._convert_to_str(key) for key, value in sequences_dict.items() if value > 1]
