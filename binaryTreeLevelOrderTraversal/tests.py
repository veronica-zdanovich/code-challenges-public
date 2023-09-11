import unittest

from parameterized import parameterized

from binaryTreeLevelOrderTraversal.binary_tree_level_order_traversal import Solution
from treeNode.tree_node import Tree


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand([
        [[3, 9, 20, None, None, 15, 7], [[15, 7], [9, 20], [3]]],
        [[1], [[1]]],
        [[], []],
        [[1, 2, 3, 4, None, None, 5], [[4, 5], [2, 3], [1]]],
        [[5, 0, -4, -1, -6, -9, None, 7, None, 1, 3, None, 0, None, 9, None, None, 6, 0, None, -7, None, None, None,
           None, None, None, -4, None, 1, None, None, -4],
         [[-4], [1], [-4], [9, 6, 0, -7], [7, 1, 3, 0], [-1, -6, -9], [0, -4], [5]]],
    ])
    def test_solution(self, input_array, expected_result):
        tree = Tree()
        head = tree.fill_in_tree(input_array)
        self.assertEqual(self.solution.levelOrderBottom(head), expected_result)


if __name__ == '__main__':
    unittest.main()
