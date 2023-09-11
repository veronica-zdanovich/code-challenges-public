from typing import List

'''
Given an array of non-negative integers arr, you are initially positioned at start index of the array. 
When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.
'''


def can_jump_to_zero(arr: List[int], index: int) -> bool:
    if arr[index] < 0:
        return False

    if arr[index] == 0:
        return True

    right_jump_index = index + arr[index]
    left_jump_index = index - arr[index]

    arr[index] = -1
    if right_jump_index < len(arr):
        if can_jump_to_zero(arr, right_jump_index):
            return True

    if left_jump_index >= 0:
        if can_jump_to_zero(arr, left_jump_index):
            return True

    return False


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        return can_jump_to_zero(arr, start)
