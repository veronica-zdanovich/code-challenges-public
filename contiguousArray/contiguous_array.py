from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_length = 0
        current_sum = 0

        sum_start_index = dict()
        sum_start_index[0] = -1

        for i in range(len(nums)):
            if nums[i] == 0:
                current_sum -= 1
            else:
                current_sum += 1

            if sum_start_index.get(current_sum) is not None:
                max_length = max(max_length, i - sum_start_index[current_sum])
            else:
                sum_start_index[current_sum] = i

        return max_length
