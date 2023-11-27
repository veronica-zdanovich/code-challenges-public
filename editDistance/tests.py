import unittest

from parameterized import parameterized

from editDistance.edit_distance import Solution
from editDistance.edit_distance_table import Solution as TableSolution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.table_solution = TableSolution()

    @parameterized.expand([
        ["word1", "word2", 1],
        ["a", "a", 0],
        ["a", "ab", 1],
        ["horse", "ros", 3],
        ["intention", "execution", 5],
        ])
    def test_solution(self, word1, word2, expected_result):
        self.assertEqual(expected_result, self.solution.minDistance(word1, word2))
        self.assertEqual(expected_result, self.table_solution.minDistance(word1, word2))
