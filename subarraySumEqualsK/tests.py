import unittest

from parameterized import parameterized

from subarraySumEqualsK.subarray_sum_equals_k import Solution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand([
        [[1, 1, 1], 2, 2],
        [[1, 2, 3], 3, 2],
        [[], 0, 0],
        [[0, 0, 0, 0, 0, 0, 0], 0, 28],
        [[1, 1, 1, 1, 1, 1, 1, 1], 4, 5],
    ])
    def test_solution(self, input_array, k, expected_result):
        self.assertEqual(expected_result, self.solution.subarraySum(input_array, k))
