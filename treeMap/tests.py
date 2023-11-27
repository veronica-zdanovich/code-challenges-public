import unittest

from parameterized import parameterized

from treeMap.tree_map import Solution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand([
        [
            ["TreeMap", "put", "remove", "get", "put", "remove", "remove", "put", "put", "get"],
            [[], [504, 155], [89], [334], [570, 521], [504], [504], [507, 661], [175, 641], [504]],
            [None, None, None, None, None, None, None, None, None, None]
        ],
        [
            ["TreeMap", "put", "put", "get", "get", "put", "get", "remove", "get"],
            [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]],
            [None, None, None, 1, None, None, 1, None, None]
        ],
        [
            ["TreeMap", "remove", "get", "put", "put", "put", "get", "put", "put", "put", "put"],
            [[], [14], [4], [7, 3], [11, 1], [12, 1], [7], [1, 19], [0, 3], [1, 8], [2, 6]],
            [None, None, None, None, None, None, 3, None, None, None, None]
        ],
        [
            ["TreeMap", "put", "put", "remove", "put", "put", "put", "put", "put", "put", "put", "put", "put", "put",
             "put", "remove", "put", "put", "get"],
            [[], [65, 65], [42, 0], [42], [17, 90], [31, 76], [48, 71], [5, 50], [7, 68], [73, 74], [85, 18], [74, 95],
             [84, 82], [59, 29], [71, 71], [42], [51, 40], [33, 76], [17]],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
             90]
        ]
    ])
    def test_solution(self, commands, args, expected_result):
        self.assertEqual(expected_result, self.solution.run_commands(commands, args))
