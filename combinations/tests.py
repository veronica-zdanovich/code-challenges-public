import unittest
from math import factorial

from parameterized import parameterized

from combinations.combinations_solution import Solution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand([
        [6, 4, [[1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 3, 6], [1, 2, 4, 5], [1, 2, 4, 6], [1, 2, 5, 6], [1, 3, 4, 5],
                [1, 3, 4, 6], [1, 3, 5, 6], [1, 4, 5, 6], [2, 3, 4, 5], [2, 3, 4, 6], [2, 3, 5, 6], [2, 4, 5, 6],
                [3, 4, 5, 6]]],
        [5, 4, [[1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 4, 5], [1, 3, 4, 5], [2, 3, 4, 5]]],
        [6, 5, [[1, 2, 3, 4, 5], [1, 2, 3, 4, 6], [1, 2, 3, 5, 6], [1, 2, 4, 5, 6], [1, 3, 4, 5, 6], [2, 3, 4, 5, 6]]],
        [5, 3, [[1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 3, 4], [1, 3, 5], [1, 4, 5], [2, 3, 4], [2, 3, 5], [2, 4, 5],
                [3, 4, 5]]],
        [5, 2, [[1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]]],
        [5, 1, [[1], [2], [3], [4], [5]]],
        ])
    def test_solution(self, n, k, expected_result):
        expected_len = factorial(n)/(factorial(n - k) * factorial(k))
        combinations = self.solution.combine(n, k)
        self.assertEqual(expected_result, combinations)
        self.assertEqual(expected_len, len(combinations))
