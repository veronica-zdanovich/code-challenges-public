from typing import List


class Solution:
    def _swap(self, left: int, right: int, nums: List[int]):
        nums[left], nums[right] = nums[right], nums[left]

    def sort_colors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_0 = 0
        middle = 0
        first_2 = len(nums) - 1

        while middle <= first_2:
            if nums[middle] < 1:
                self._swap(middle, last_0, nums)
                middle += 1
                last_0 += 1
            elif nums[middle] == 1:
                middle += 1
            elif nums[middle] > 1:
                self._swap(middle, first_2, nums)
                first_2 -= 1
