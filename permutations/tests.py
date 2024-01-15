import unittest

from parameterized import parameterized

from permutations.permutations_solutions import Solution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand([
        [[1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]],
        [[1], [[1]]],
        [[1, 2], [[1, 2], [2, 1]]],
        [[1, 2, 3, 4], [[1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 2, 3], [1, 4, 3, 2], [2, 1, 3, 4],
                        [2, 1, 4, 3], [2, 3, 1, 4], [2, 3, 4, 1], [2, 4, 1, 3], [2, 4, 3, 1], [3, 1, 2, 4], [3, 1, 4, 2],
                        [3, 2, 1, 4], [3, 2, 4, 1], [3, 4, 1, 2], [3, 4, 2, 1], [4, 1, 2, 3], [4, 1, 3, 2], [4, 2, 1, 3],
                        [4, 2, 3, 1], [4, 3, 1, 2], [4, 3, 2, 1]]],
    ])
    def test_solution(self, input_array, expected_result):
        self.assertEqual(expected_result, self.solution.permute(input_array))


if __name__ == '__main__':
    unittest.main()
