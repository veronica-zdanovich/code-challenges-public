import unittest

from parameterized import parameterized

from dailyTemperatures.daily_temperatures import Solution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand([
        [[73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]],
        [[30, 40, 50, 60], [1, 1, 1, 0]],
        [[30, 60, 90], [1, 1, 0]],
        [[30, 90], [1, 0]],
    ])
    def test_solution(self, input_array, expected_result):
        self.assertEqual(expected_result, self.solution.dailyTemperatures(input_array))
