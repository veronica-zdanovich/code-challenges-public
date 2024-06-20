import unittest

from parameterized import parameterized

from setMatrixZeroes.set_matrix_zeroes import Solution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand([
        [[[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]]],
        [[[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]], [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]],
        [[[1, 0, 3]], [[0, 0, 0]]],
        [[[0, 0, 0, 5], [4, 3, 1, 4], [0, 1, 1, 4], [1, 2, 1, 3], [0, 0, 1, 1]],
         [[0, 0, 0, 0], [0, 0, 0, 4], [0, 0, 0, 0], [0, 0, 0, 3], [0, 0, 0, 0]]],
        [[[-5, 7, 2147483647, 3], [0, 3, 6, -2147483648], [8, 3, -3, -6], [-9, -9, 8, 0]],
         [[0, 7, 2147483647, 0], [0, 0, 0, 0], [0, 3, -3, 0], [0, 0, 0, 0]]],
    ])
    def test_solution(self, matrix, expected_result):
        self.solution.setZeroes(matrix)
        self.assertEqual(expected_result, matrix)
