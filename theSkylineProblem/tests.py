import unittest

from parameterized import parameterized

from theSkylineProblem.the_skyline_problem import Solution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand([
        [[[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]],
         [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]],
        [[[0, 2, 3], [2, 5, 3]], [[0, 3], [5, 0]]],
        [[[0, 1, 3]], [[0, 3], [1, 0]]],
        [[[2, 9, 10], [9, 12, 15]], [[2, 10], [9, 15], [12, 0]]],
        [[[1, 2, 1], [1, 2, 2], [1, 2, 3]], [[1, 3], [2, 0]]],
        [[[3, 7, 8], [3, 8, 7], [3, 9, 6], [3, 10, 5], [3, 11, 4], [3, 12, 3], [3, 13, 2], [3, 14, 1]],
         [[3, 8], [7, 7], [8, 6], [9, 5], [10, 4], [11, 3], [12, 2], [13, 1], [14, 0]]]
    ])
    def test_solution(self, buildings, expected_result):
        self.assertEqual(expected_result, self.solution.getSkyline(buildings))
