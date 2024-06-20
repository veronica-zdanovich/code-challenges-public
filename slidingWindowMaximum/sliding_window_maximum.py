from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_deque = deque()
        max_deque.append(0)
        max_sliding_window = list()

        if k == 1:
            return nums

        for i in range(1, len(nums)):
            max_element_index = max_deque[0]
            if i - max_element_index >= k:
                max_deque.popleft()

            new_element = nums[i]
            while len(max_deque) > 0 and nums[max_deque[-1]] < new_element:
                max_deque.pop()

            max_deque.append(i)

            if i < k - 1:
                continue

            max_element_index = max_deque[0]
            max_sliding_window.append(nums[max_element_index])

        return max_sliding_window
