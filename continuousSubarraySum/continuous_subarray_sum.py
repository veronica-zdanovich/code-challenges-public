from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for index, num in enumerate(nums):
            if index == 0:
                continue
            else:
                nums[index] = nums[index - 1] + num

        duplicates_set = set()
        prev_remainder = nums[0] % k

        for index in range(1, len(nums)):
            remainder = nums[index] % k
            nums[index] = remainder

            if remainder == 0:
                return True

            if remainder in duplicates_set:
                return True

            duplicates_set.add(prev_remainder)
            prev_remainder = remainder

        return False
