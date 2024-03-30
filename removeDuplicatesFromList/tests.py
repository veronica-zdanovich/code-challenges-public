import unittest

from parameterized import parameterized

from removeDuplicatesFromList.remove_duplicates_from_list import Solution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand([
        [[1, 5, 3, 6, 3, 5, 6, 1], [1, 5, 3, 6]],
        [[0, 0, 0], [0]],
        [[1, 2, 3], [1, 2, 3]],
        ])
    def test_solution(self, input_list, expected_result):
        self.assertEqual(expected_result, self.solution.remove_duplicates(input_list))
