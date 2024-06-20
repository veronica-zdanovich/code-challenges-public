import unittest

from parameterized import parameterized

from TreeNode import Tree
from binaryTreeMaximumPathSum.binary_tree_maximum_path_sum import Solution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand([
        [[5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 48],
        [[-2, 1], 1],
        [[1, 2, None, 3, None, 4, None, 5], 15],
        [[-10, 9, 20, None, None, 15, 7], 42],
        [[1, 2, 3], 6],
    ])
    def test_solution(self, input_array, expected_result):
        tree = Tree()
        root = tree.fill_in_tree(input_array)
        self.assertEqual(expected_result, self.solution.maxPathSum(root))
