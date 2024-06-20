from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = list()

        for n in nums:
            n = abs(n)
            if nums[n - 1] < 0:
                duplicates.append(n)
            nums[n - 1] *= -1

        return duplicates
