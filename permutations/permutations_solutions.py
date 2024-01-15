from typing import List


class Solution:
    def backtracking(self, nums: List[int], path: List[int], result: List[List[int]]):
        if len(path) == len(nums):
            result.append(path[:])
            return True

        if len(nums) == 0:
            return

        for num in nums:
            if num in path:
                continue

            path.append(num)
            self.backtracking(nums, path, result)
            path.pop()

        return False

    def permute(self, nums: List[int]) -> List[List[int]]:
        result = list()
        path = list()
        self.backtracking(nums, path, result)
        return result
