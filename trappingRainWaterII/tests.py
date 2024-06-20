import unittest

from parameterized import parameterized

from trappingRainWaterII.trapping_rain_water import Solution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand([
        [[[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]], 4],
        [[[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [3, 2, 1, 2, 3], [3, 2, 2, 2, 3], [3, 3, 3, 3, 3]], 10],
        [[[12, 13, 1, 12], [13, 4, 13, 12], [13, 8, 10, 12], [12, 13, 12, 12], [13, 13, 13, 13]], 14],
        [[[5, 5, 5, 1], [5, 1, 1, 5], [5, 1, 5, 5], [5, 2, 5, 8]], 3],
    ])
    def test_solution(self, input_array, expected_result):
        self.assertEqual(expected_result, self.solution.trapRainWater(input_array))


if __name__ == '__main__':
    unittest.main()