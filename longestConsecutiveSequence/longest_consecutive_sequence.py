from typing import List

from dsu.dsu import DSU


class UnionFind(DSU):
    def __init__(self, max_size: int):
        self.max_rank = 0
        super().__init__(max_size)

    def add(self, id: int):
        self.insert(id)
        self.max_rank = max(self.max_rank, self.ranks[id])

    def union(self, p: int, q: int):
        p_root = self.find_root(p)
        q_root = self.find_root(q)
        if p_root == q_root:
            return

        self.join(p_root, q_root)
        new_rank = max(self.ranks[p_root], self.ranks[q_root])
        self.max_rank = max(self.max_rank, new_rank)

    def get_max_rank(self) -> int:
        return self.max_rank


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        size = len(nums)
        if size < 2:
            return size

        union_find = UnionFind(size)
        nums_dict = dict()
        for index, num in enumerate(nums):
            repeat = nums_dict.get(num, None)
            if repeat is not None:
                continue

            nums_dict[num] = index
            union_find.add(index)

            previous_index = nums_dict.get(num - 1, None)
            if previous_index is not None:
                union_find.union(previous_index, index)

            next_index = nums_dict.get(num + 1, None)
            if next_index is not None:
                union_find.union(next_index, index)

        return union_find.get_max_rank()
