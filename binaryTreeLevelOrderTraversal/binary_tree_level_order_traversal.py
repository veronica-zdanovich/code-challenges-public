from queue import Queue
from typing import Optional, List

from treeNode.tree_node import TreeNode, Tree

'''
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. 
(i.e., from left to right, level by level from leaf to root).

Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]
'''


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result

        queue = Queue()
        parent_node_level = 0

        queue.put({"node": root, "level": parent_node_level})
        result.append([root.val])

        children_nodes = []

        while not queue.empty():
            first_element = queue.get()
            current_node = first_element["node"]
            current_level = first_element["level"]

            if current_level != parent_node_level and len(children_nodes) > 0:
                result.append(children_nodes)
                children_nodes = []
                parent_node_level = current_level

            if current_node.left:
                queue.put(({"node": current_node.left, "level": current_level + 1}))
                children_nodes.append(current_node.left.val)

            if current_node.right:
                queue.put(({"node": current_node.right, "level": current_level + 1}))
                children_nodes.append(current_node.right.val)

        result.reverse()
        return result
