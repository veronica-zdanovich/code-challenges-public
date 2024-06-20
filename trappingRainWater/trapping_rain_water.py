from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left_border_index = 0
        right_border_index = len(height) - 1
        left_bound = 0
        right_bound = 0
        trapped_water = 0

        while left_border_index < right_border_index:
            if height[left_border_index] < height[right_border_index]:
                left_bound = max(height[left_border_index], left_bound)
                if height[left_border_index] != left_bound:
                    trapped_water += left_bound - height[left_border_index]

                left_border_index += 1

            else:
                right_bound = max(height[right_border_index], right_bound)
                if height[right_border_index] != right_bound:
                    trapped_water += right_bound - height[right_border_index]

                right_border_index -= 1

        return trapped_water
