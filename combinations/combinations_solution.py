from typing import List


class Solution:
    def __init__(self):
        self.n = 0
        self.k = 0
        self.combinations = list()

    def find_combination(self, seq: List, start_num: int):
        if len(seq) == self.k:
            self.combinations.append(seq)
            return seq[:-1]

        for i in range(start_num, self.n + 1):
            seq.append(i)
            seq = self.find_combination(seq, i + 1)

        return seq[:-1]

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.n = n
        self.k = k
        seq = list()
        self.find_combination(seq, 1)
        return self.combinations
