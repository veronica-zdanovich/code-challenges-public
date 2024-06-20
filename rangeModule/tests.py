import unittest

from parameterized import parameterized

from rangeModule.range_module import Solution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand([
        [["RangeModule", "addRange", "queryRange", "removeRange", "removeRange", "addRange"],
         [[], [5, 8], [3, 4], [5, 6], [3, 6], [1, 3]],
         [None, None, False, None, None, None]],
        [["RangeModule", "addRange", "queryRange", "removeRange", "removeRange", "addRange", "queryRange", "addRange",
          "queryRange", "removeRange"],
         [[], [5, 8], [3, 4], [5, 6], [3, 6], [1, 3], [2, 3], [4, 8], [2, 3], [4, 9]],
         [None, None, False, None, None, None, True, None, True, None]],
        [["RangeModule", "addRange", "addRange", "addRange", "queryRange", "queryRange", "queryRange", "removeRange",
          "queryRange"],
         [[], [10, 180], [150, 200], [250, 500], [50, 100], [180, 300], [600, 1000], [50, 150], [600, 1000]],
         [None, None, None, None, True, False, False, None, False]],
    ])
    def test_solution(self, commands, args, expected_result):
        self.assertEqual(expected_result, self.solution.run_commands(commands, args))
