import unittest

from parameterized import parameterized

from slidingWindowMaximum.sliding_window_maximum import Solution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand([
        [[9, 6, 11, 8, 10, 9, 14, 93], 4, [11, 11, 11, 14, 93]],
        [[1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]],
        [[1, -1], 1, [1, -1]],
        [[7, 2, 4], 2, [7, 4]],
        [[9, 10, 9, -7, -4, -8, 2, -6], 5, [10, 10, 9, 2]],
    ])
    def test_solution(self, input_nums, k, expected_result):
        self.assertEqual(expected_result, self.solution.maxSlidingWindow(input_nums, k))

