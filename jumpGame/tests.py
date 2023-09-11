import unittest

from parameterized import parameterized

from jumpGame.jump_game import Solution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand([
        [[4, 2, 3, 0, 3, 1, 2], 5, True],
        [[4, 2, 3, 0, 3, 1, 2], 0, True],
        [[3, 0, 2, 1, 2], 2, False],
        [[0, 1], 1, True],
        [[4, 4, 1, 3, 0, 3], 2, True],
        [[2, 2, 3, 2, 3], 3, False],
    ])
    def test_solution(self, input_array, start, expected_result):
        self.assertEqual(self.solution.canReach(input_array, start), expected_result)


if __name__ == '__main__':
    unittest.main()
