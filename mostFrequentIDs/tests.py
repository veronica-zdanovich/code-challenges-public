import unittest

from parameterized import parameterized

from mostFrequentIDs.most_frequent_ids import Solution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand([
        [[5, 5, 3], [2, -2, 1], [2, 0, 1]],
        [[7, 7], [3, 5], [3, 8]],
        [[2, 3, 2, 1], [3, 2, -3, 1], [3, 3, 2, 2]],
        [[2, 9, 9], [5, 4, -3], [5, 5, 5]],
    ])
    def test_solution(self, nums, freq, expected_result):
        self.assertEqual(expected_result, self.solution.mostFrequentIDs(nums, freq))

