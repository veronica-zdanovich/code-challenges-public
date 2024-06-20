import unittest

from parameterized import parameterized

from findAllDuplicatesInAnArray.find_all_duplicates_in_an_array import Solution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand([
        [[1, 2, 5, 7, 7, 8, 8, 10, 6, 3], [7, 8]],
        [[], []],
        [[1, 2], []],
        [[1, 2, 2], [2]],
        [[4, 3, 2, 7, 8, 2, 3, 1], [2, 3]],
        [[1, 2, 2, 3, 4, 4], [2, 4]],
        ])
    def test_solution(self, nums, expected_result):
        self.assertEqual(expected_result, self.solution.findDuplicates(nums))
