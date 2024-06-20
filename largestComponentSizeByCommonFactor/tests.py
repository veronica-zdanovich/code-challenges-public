import unittest

from parameterized import parameterized

from largestComponentSizeByCommonFactor.largest_component_size_by_common_factor import Solution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand([
        [[4, 6, 15, 35], 4],
        [[5, 7, 8, 10], 3],
        [[2, 3, 6, 7, 4, 12, 21, 39], 8],
        [[1, 3], 1],
        [[20, 50, 9, 63], 2],
        [[1, 2, 3, 4, 5, 9], 2],
        [[1, 2, 3, 4], 2],
        ])
    def test_solution(self, nums, expected_result):
        self.assertEqual(expected_result, self.solution.largestComponentSize(nums))
