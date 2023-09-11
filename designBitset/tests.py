import unittest
from designBitset.design_bitset import Solution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        commands = ["Bitset", "flip", "unfix", "all", "fix", "fix", "unfix", "all", "count", "toString", "toString",
                    "toString", "unfix", "flip", "all", "unfix", "one", "one", "all", "fix", "unfix"]
        args = [[2], [], [1], [], [1], [1], [1], [], [], [], [], [], [0], [], [], [0], [], [], [], [0], [0]]
        expected_result = [None, None, None, False, None, None, None, False, 1, "10", "10", "10", None, None, True,
                           None, True, True, False, None, None]
        self.solution.run_commands(commands, args)
        self.assertEqual(self.solution.show_output(), expected_result)

    def test_2(self):
        commands = ["Bitset", "fix", "fix", "flip", "all", "unfix", "flip", "one", "unfix", "count", "toString"]
        args = [[5], [3], [1], [], [], [0], [], [], [0], [], []]
        expected_result = [None, None, None, None, False, None, None, True, None, 2, "01010"]
        self.solution.run_commands(commands, args)
        self.assertEqual(self.solution.show_output(), expected_result)

    def test_3(self):
        commands = ["Bitset", "unfix", "unfix", "count", "one", "toString", "count", "toString", "unfix", "flip",
                    "toString", "flip", "fix", "unfix", "unfix", "toString", "fix", "toString", "fix", "count", "fix",
                    "unfix", "flip", "unfix", "fix", "flip", "unfix", "count", "fix", "count", "all", "all", "unfix",
                    "flip", "all", "count", "count", "one", "unfix", "one", "count"]
        args = [[90], [0], [62], [], [], [], [], [], [72], [], [], [], [11], [80], [80], [], [55], [], [87], [], [61],
                [0], [], [67], [40], [], [5], [], [14], [], [], [], [69], [], [], [], [], [], [71], [], []]
        expected_result = [None, None, None, 0, False,
                           "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
                           0,
                           "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
                           None, None,
                           "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",
                           None, None, None, None,
                           "000000000001000000000000000000000000000000000000000000000000000000000000000000000000000000",
                           None,
                           "000000000001000000000000000000000000000000000000000000010000000000000000000000000000000000",
                           None, 3, None, None, None, None, None, None, None, 5, None, 6, False, False, None, None,
                           False, 84, 84, True, None, True, 83]
        self.solution.run_commands(commands, args)
        self.assertEqual(self.solution.show_output(), expected_result)


if __name__ == '__main__':
    unittest.main()
