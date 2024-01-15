import unittest

from parameterized import parameterized

from compressArray.compress_array import Solution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand([
        [["a","b","b","b","b","b","b","b","b","b","b","b","b"], 4],
        [["a", "a", "b", "b", "c", "c", "c"], 6],
        [["a", "a", "a", "b", "b", "a", "a"], 6],
        [["a", "b", "c"], 3],
        [["a", "a", "a", "b"], 3],
        ])
    def test_solution(self, chars, expected_result):
        self.assertEqual(expected_result, self.solution.compress(chars))
