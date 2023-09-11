import unittest

from parameterized import parameterized

from numIslands.num_islands import Solution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand([
        [[
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ], 3],
        [[
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ], 1],
        [[["0"]], 0],
        [[["0", "1", "0"]], 1],
        [[["0", "1", "0"], ["0", "0", "1"]], 2],
    ])
    def test_solution(self, grid, expected_result):
        self.assertEqual(self.solution.num_islands(grid), expected_result)


if __name__ == '__main__':
    unittest.main()
