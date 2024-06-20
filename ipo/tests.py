import unittest

from parameterized import parameterized

from ipo.ipo_solution import Solution


class Tests(unittest.TestCase):
    @parameterized.expand([
        [2, 0, [1, 2, 3], [0, 1, 1], 4],
        [3, 0, [1, 2, 3], [0, 1, 2], 6],
        [1, 0, [1, 2, 3], [0, 1, 2], 1],
        [1, 0, [1, 2, 3], [1, 1, 2], 0],
        ])
    def test_solution(self, k, w, capital, profits, expected_result):
        self.solution = Solution()
        self.assertEqual(expected_result, self.solution.findMaximizedCapital(k, w, capital, profits))
