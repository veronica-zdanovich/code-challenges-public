from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_element = max(nums)
        count_subarrays = 0

        start = 0
        end = 0
        max_appearance_count = 0
        while end < len(nums):
            if nums[end] == max_element:
                max_appearance_count += 1
            while max_appearance_count >= k:
                count_subarrays += len(nums) - end
                if nums[start] == max_element:
                    max_appearance_count -= 1
                start += 1
            end += 1
        return count_subarrays
