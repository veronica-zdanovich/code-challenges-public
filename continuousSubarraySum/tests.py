import unittest

from parameterized import parameterized

from continuousSubarraySum.continuous_subarray_sum import Solution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand([
        [[23, 2, 6, 4, 5, 1], 6, True],
        [[23, 2, 6, 4, 7], 13, False],
        [[0], 1, False],
        [[0, 0], 1, True],
        [[2, 4, 3], 6, True],
        [[405, 504, 203, 96, 43, 50, 214, 327, 120, 345, 33, 314, 377, 62, 431, 379, 114, 208, 106, 345, 391, 513, 9,
          405, 452, 186, 295, 33, 423, 122, 355, 311, 192, 429, 320, 360, 85, 96, 32, 258, 407, 71, 436, 370, 365, 199,
          443, 521, 262, 232, 355, 241, 250, 10, 258, 324, 335, 446, 474, 385, 74, 101, 111, 162, 349, 149, 51, 399,
          371, 139, 199, 264, 118, 155, 134, 518, 388, 113, 520, 441, 384, 449, 14, 104, 267, 92, 477, 50, 505, 368,
          466, 519, 105, 443, 31, 21, 485, 146, 115, 94], 337, True],
        ])
    def test_solution(self, input_array, k, expected_result):
        self.assertEqual(expected_result, self.solution.checkSubarraySum(input_array, k))
