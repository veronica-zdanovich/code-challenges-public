import unittest
from parameterized import parameterized
from countServersThatCommunicate.count_servers_that_communicate import Solution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand([
        [[[1, 0, 0, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0]], 3],
        [[[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]], 4],
        [[[1, 0], [1, 1]], 3],
        [[[1, 0], [0, 1]], 0],
        [[[0, 0, 1, 0, 1], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0], [1, 0, 0, 1, 1], [0, 0, 1, 1, 0]], 12],
        ])
    def test_solution(self, input_grid, expected_result):
        self.assertEqual(expected_result, self.solution.countServers(input_grid))
