import unittest

from parameterized import parameterized

from randomizedSet.randomized_set import Solution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand([
        [
            ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"],
            [[], [1], [2], [2], [], [1], [2], []],
            [[None, True, False, True, 1, True, False, 2], [None, True, False, True, 2, True, False, 2]]
        ],
        [
            ["RandomizedSet", "insert", "insert", "remove", "insert", "remove", "getRandom"],
            [[], [0], [1], [0], [2], [1], []],
            [[None, True, True, True, True, True, 2]]
        ]
    ])
    def test_solution(self, commands, args, expected_result):
        self.assertIn(self.solution.run_commands(commands, args), expected_result)
