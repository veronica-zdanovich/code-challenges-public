import unittest

from parameterized import parameterized

from spiralMatrix.spiral_matrix import Solution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand([
        [[[7], [9], [6]], [7, 9, 6]],
        [[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]],
        [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]],
    ])
    def test_solution(self, matrix, expected_result):
        self.assertEqual(expected_result, self.solution.spiralOrder(matrix))


if __name__ == '__main__':
    unittest.main()
