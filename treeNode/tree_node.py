from queue import Queue
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.head = None

    def fill_in_tree(self, values):
        if len(values) == 0:
            return []

        index = 0
        queue = Queue()
        self.head = TreeNode(values[index])
        queue.put(self.head)

        while not queue.empty():
            current_node = queue.get()
            index = self.fill_in_subtree(current_node, index, values, queue)
            if index < 0:
                break

        return self.head

    def fill_in_subtree(self, node: TreeNode, index: int, values: List[int], queue: Queue) -> int:
        if index + 2 >= len(values):
            return -1

        if node.left is None and values[index + 1] is not None:
            node.left = TreeNode(values[index + 1])
            queue.put(node.left)

        if node.right is None and values[index + 2] is not None:
            node.right = TreeNode(values[index + 2])
            queue.put(node.right)

        return index + 2
