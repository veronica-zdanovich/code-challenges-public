import unittest

from parameterized import parameterized

from contiguousArray.contiguous_array import Solution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand([
        [[0, 0, 1, 0, 0, 0, 1, 1], 6],
        [[0, 1, 0, 1], 4],
        [[0, 1, 0, 1, 0, 0, 0, 1, 0], 4],
        [[1, 0, 0, 0, 0, 0], 2],
        [[1, 0, 0, 0, 1, 0, 1, 1, 1], 8],
        ])
    def test_solution(self, nums, expected_result):
        self.assertEqual(expected_result, self.solution.findMaxLength(nums))