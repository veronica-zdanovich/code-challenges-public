import unittest

from parameterized import parameterized

from minStack.min_stack import MinStack
from minStack.min_stack_dict import MinStack as MinStackDict
from minStack.solution import Solution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand([
        [
            ["MinStack", "push", "push", "getMin", "getMin", "push", "getMin", "getMin", "top", "getMin", "pop", "push",
             "push", "getMin", "push", "pop", "top", "getMin", "pop"],
            [[], [-10], [14], [], [], [-20], [], [], [], [], [], [10], [-7], [], [-7], [], [], [], []],
            [None, None, None, -10, -10, None, -20, -20, -20, -20, None, None, None, -10, None, None, -7, -10, None]
        ],
        [
            ["MinStack", "push", "push", "push", "top", "pop", "getMin", "pop", "getMin", "pop", "push", "top",
             "getMin", "push", "top", "getMin", "pop", "getMin"],
            [[], [2147483646], [2147483646], [2147483647], [], [], [], [], [], [], [2147483647], [], [], [-2147483648],
             [], [], [], []],
            [None, None, None, None, 2147483647, None, 2147483646, None, 2147483646, None, None, 2147483647, 2147483647,
             None, -2147483648, -2147483648, None, 2147483647]
        ],
        [
            ["MinStack", "push", "push", "push", "getMin", "pop", "getMin"],
            [[], [0], [1], [0], [], [], []],
            [None, None, None, None, 0, None, 0]
        ],
        [
            ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"],
            [[], [-2], [0], [-3], [], [], [], []],
            [None, None, None, None, -3, None, 0, -2]
        ],
        [
            ["MinStack", "push", "push", "push", "push", "getMin", "pop", "getMin", "pop", "getMin", "pop", "getMin"],
            [[], [2], [0], [3], [0], [], [], [], [], [], [], []],
            [None, None, None, None, None, 0, None, 0, None, 0, None, 2]
        ],
        [
            ["MinStack", "push", "push", "push", "push", "pop", "getMin", "pop", "getMin", "pop", "getMin"],
            [[], [512], [-1024], [-1024], [512], [], [], [], [], [], []],
            [None, None, None, None, None, None, -1024, None, -1024, None, 512]
        ]
    ])
    def test_solution(self, commands, args, expected_result):
        self.assertEqual(expected_result, self.solution.run_commands(commands, args, MinStack))
        self.assertEqual(expected_result, self.solution.run_commands(commands, args, MinStackDict))
