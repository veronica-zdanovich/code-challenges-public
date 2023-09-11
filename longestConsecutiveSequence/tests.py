import unittest

from parameterized import parameterized

from longestConsecutiveSequence.longest_consecutive_sequence import Solution
from longestConsecutiveSequence.longest_consecutive_sequence_set import Solution as SetSolution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.set_solution = SetSolution()

    @parameterized.expand([
        [[100, 4, 200, 1, 3, 2], 4],
        [[0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9],
        [[0], 1],
        [[0, 0], 1],
        [[2, 4, 3], 3],
        [[], 0],
        [[1, -8, 7, -2, -4, -4, 6, 3, -4, 0, -7, -1, 5, 1, -9, -3], 6]
    ])
    def test_solution(self, input_array, expected_result):
        self.assertEqual(expected_result, self.solution.longestConsecutive(input_array))

    @parameterized.expand([
        [[100, 4, 200, 1, 3, 2], 4],
        [[0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9],
        [[0], 1],
        [[0, 0], 1],
        [[2, 4, 3], 3],
        [[], 0],
        [[1, -8, 7, -2, -4, -4, 6, 3, -4, 0, -7, -1, 5, 1, -9, -3], 6]
    ])
    def test_set_solution(self, input_array, expected_result):
        self.assertEqual(expected_result, self.set_solution.longestConsecutive(input_array))

