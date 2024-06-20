import unittest

from parameterized import parameterized

from trappingRainWater.trapping_rain_water import Solution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand([
        [[4, 2, 0, 3, 2, 5], 9],
        [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6],
        [[0], 0],
        [[3, 0, 1, 0], 1],
        [[5, 2, 5, 3, 5, 3, 1, 1, 3], 9],
    ])
    def test_solution(self, input_array, expected_result):
        self.assertEqual(expected_result, self.solution.trap(input_array))


if __name__ == '__main__':
    unittest.main()
