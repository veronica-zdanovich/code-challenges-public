from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarray_sums = defaultdict(int)
        subarray_amount = 0

        current_sum = 0
        for index, num in enumerate(nums):
            current_sum += num

            if current_sum == k:
                subarray_amount += 1

            if subarray_sums.get(current_sum - k) is not None:
                subarray_amount += subarray_sums[current_sum - k]

            subarray_sums[current_sum] += 1

        return subarray_amount
