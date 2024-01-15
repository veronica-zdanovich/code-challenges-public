import unittest

from parameterized import parameterized

from searchInRotatedSortedArray.search_in_rotated_sorted_array import Solution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand([
        [[4, 5, 6, 7, 0, 1, 2], 0, 4],
        [[4, 5, 6, 7, 0, 1, 2], 3, -1],
        [[1], 0, -1],
        [[5, 1, 3], 5, 0],
        [[4, 5, 6, 7, 8, 1, 2, 3], 8, 4],
    ])
    def test_solution(self, nums, target, expected_result):
        self.assertEqual(expected_result, self.solution.search(nums, target))


if __name__ == '__main__':
    unittest.main()
