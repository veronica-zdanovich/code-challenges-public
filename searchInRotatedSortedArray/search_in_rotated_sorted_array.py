from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (right + left) // 2

            if target == nums[middle]:
                return middle

            if nums[middle] <= nums[right] and nums[middle] < target <= nums[right] :  # right part is sorted
                left = middle + 1
                continue

            if nums[left] <= nums[middle] and nums[left] <= target < nums[middle]:  # left part is sorted
                right = middle - 1
                continue

            if nums[left] >= nums[middle] and target > nums[middle]:  # left part is unsorted
                right = middle - 1
                continue

            if nums[middle] >= nums[right] and target < nums[middle]:  # right part is unsorted
                left = middle + 1
                continue

            left += 1

        return -1
