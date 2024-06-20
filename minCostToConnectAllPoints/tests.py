import unittest

from parameterized import parameterized

from minCostToConnectAllPoints.kruskals import Solution as KruskalsAlgorithm
from minCostToConnectAllPoints.prims import Solution as PrimsAlgorithm


class Tests(unittest.TestCase):
    def setUp(self):
        self.kruskals_algorithm_solution = KruskalsAlgorithm()
        self.prims_algorithm_solution = PrimsAlgorithm()

    @parameterized.expand([
        [[[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]], 20],
        [[[3, 12], [-2, 5], [-4, 1]], 18],
        [[[0, 0], [1, 1], [1, 0], [-1, 1]], 4],
        [[[2, -3], [-17, -8], [13, 8], [-17, -15]], 53],
        [[[7, 18], [-15, 19], [-18, -15], [-7, 14], [4, 1], [-6, 3]], 85],
        [[[-14, -14], [-18, 5], [18, -10], [18, 18], [10, -2]], 102]
    ])
    def test_solution(self, input_points, expected_result):
        self.assertEqual(self.kruskals_algorithm_solution.minCostConnectPoints(input_points), expected_result)
        self.assertEqual(self.prims_algorithm_solution.minCostConnectPoints(input_points), expected_result)
