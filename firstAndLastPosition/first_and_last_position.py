from typing import List


class Solution:
    def binary_search(self, nums: List[int], target: int, is_asc: bool):
        start_index = 0
        end_index = len(nums)
        target_index = -1

        while start_index <= end_index:
            middle = start_index + (end_index - start_index) // 2

            if middle == len(nums) or middle < 0:
                return target_index

            if target == nums[middle]:
                target_index = middle
                end_index = middle - 1 if is_asc else end_index
                start_index = start_index if is_asc else middle + 1
            elif target > nums[middle]:
                start_index = middle + 1
            else:
                end_index = middle - 1

        return target_index

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binary_search(nums, target, True)
        right = self.binary_search(nums, target, False)

        answers = [left, right]
        return answers
