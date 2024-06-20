from typing import List

import math


class UnionFind:
    def __init__(self, length: int):
        self.roots = [i for i in range(length)]
        self.ranks = [1 for _ in range(length)]
        self.max_rank = 1

    def find_root(self, i: int) -> int:
        while i != self.roots[i]:
            self.roots[i] = self.roots[self.roots[i]]
            i = self.roots[i]
        return i

    def join(self, i: int, j: int):
        root_i = self.find_root(i)
        root_j = self.find_root(j)

        if root_i == root_j:
            return

        if self.ranks[root_i] > self.ranks[root_j]:
            self.ranks[root_i] += self.ranks[root_j]
            self.roots[root_j] = root_i
            self.max_rank = max(self.max_rank, self.ranks[root_i])
        else:
            self.ranks[root_j] += self.ranks[root_i]
            self.roots[root_i] = root_j
            self.max_rank = max(self.max_rank, self.ranks[root_j])


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        union_find = UnionFind(len(nums))
        divisor_index_map = dict()

        for i, num in enumerate(nums):
            divisors_list = set()
            for divisor in range(2, int(math.sqrt(num)) + 1):
                if num % divisor == 0:
                    divisors_list.add(divisor)
                    if num // divisor != divisor:
                        divisors_list.add(num // divisor)
            divisors_list.add(num)

            for divisor in divisors_list:
                if divisor_index_map.get(divisor) is not None:
                    union_find.join(i, divisor_index_map[divisor])
                else:
                    divisor_index_map[divisor] = i

        return union_find.max_rank
