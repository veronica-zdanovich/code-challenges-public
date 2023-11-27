import unittest

from parameterized import parameterized

from firstAndLastPosition.first_and_last_position import Solution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand([
        [[5, 7, 7, 8, 8, 10], 8, [3, 4]],
        [[5, 7, 7, 8, 8, 10], 6, [-1, -1]],
        [[], 0, [-1, -1]],
        [[1, 3], 1, [0, 0]],
        [[1, 2, 2], 2, [1, 2]],
        [[1, 2, 3, 3, 3, 3, 4, 5, 9], 3, [2, 5]],
        [[1, 2, 2, 3, 4, 4, 4], 4, [4, 6]],
        ])
    def test_solution(self, nums, target, expected_result):
        self.assertEqual(expected_result, self.solution.searchRange(nums, target))
