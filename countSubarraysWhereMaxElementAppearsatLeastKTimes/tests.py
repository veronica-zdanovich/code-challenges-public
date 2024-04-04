import unittest

from parameterized import parameterized

from countSubarraysWhereMaxElementAppearsatLeastKTimes.count_subarrays_where_max_element_appears_at_least_k_times import \
    Solution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand([
        [[1, 3, 2, 3, 3], 2, 6],
        [[1, 4, 2, 1], 3, 0],
        [[61, 23, 38, 23, 56, 40, 82, 56, 82, 82, 82, 70, 8, 69, 8, 7, 19, 14, 58, 42, 82, 10, 82, 78, 15, 82], 2, 224],
    ])
    def test_solution(self, nums, k, expected_result):
        self.assertEqual(expected_result, self.solution.countSubarrays(nums, k))
