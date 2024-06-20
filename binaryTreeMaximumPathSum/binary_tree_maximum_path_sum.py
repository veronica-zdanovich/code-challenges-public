from typing import Optional

from TreeNode import TreeNode, Tree


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max_sum = -float("inf")

    def sum_combination(self, node: Optional[TreeNode], prev_sum):
        if node is None:
            return 0

        max_left = self.sum_combination(node.left, prev_sum + node.val)
        max_right = self.sum_combination(node.right, prev_sum + node.val)

        self.max_sum = max(self.max_sum, max_right + max_left + node.val)
        return max(node.val + max(max_left, max_right), 0)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.sum_combination(root, root.val)
        return self.max_sum
