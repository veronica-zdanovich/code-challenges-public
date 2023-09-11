from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        size = len(nums)
        if size < 2:
            return size

        max_sequence = 0
        current_sequence = 0
        nums = set(nums)

        for num in nums:
            if num - 1 in nums:
                continue
            current_sequence += 1
            while num + 1 in nums:
                current_sequence += 1
                num += 1
            max_sequence = max(max_sequence, current_sequence)
            current_sequence = 0
        return max_sequence
