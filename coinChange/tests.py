import unittest

from parameterized import parameterized

from coinChange.coin_change import Solution
from coinChange.coin_change_table import Solution as TableSolution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.table_solution = TableSolution()

    @parameterized.expand([
        [[1, 2, 5], 11, 3],
        [[1, 2, 5], 10, 2],
        [[2], 3, -1],
        [[1], 0, 0],
        [[1, 2, 5], 100, 20],
        [[186, 419, 83, 408], 6249, 20],
        [[411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422], 9864, 24],
        [[58, 92, 387, 421, 194, 208, 231], 7798, 21],
        [[470, 18, 66, 301, 403, 112, 360], 8235, 20],
        [[1, 22345647556432], 2, 2],
        ])
    def test_solution(self, coins, amount, expected_result):
        self.assertEqual(expected_result, self.solution.coinChange(coins, amount))
        self.assertEqual(expected_result, self.table_solution.coinChange(coins, amount))
