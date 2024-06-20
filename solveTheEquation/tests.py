import unittest

from parameterized import parameterized

from solveTheEquation.solve_the_equation import Solution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand([
        ["x+5-3+x=6+x-2", "x=2"],
        ["x=x", "Infinite solutions"],
        ["2x=x", "x=0"],
        ["x=x+2", "No solution"],
        ["x+3x-8=0", "x=2"],
    ])
    def test_solution(self, equation, expected_result):
        self.assertEqual(expected_result, self.solution.solveEquation(equation))
