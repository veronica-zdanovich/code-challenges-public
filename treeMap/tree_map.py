from typing import List, Optional, Tuple


class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class TreeMap:
    def __init__(self):
        self.root = None
        self.length = 0

    def __delitem__(self, key):
        self.remove(key)

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.set(key, value)

    def __len__(self):
        return self.length

    def __iter__(self):
        return self._inorder_generator(self.root)

    def _inorder_generator(self, node):
        if node is not None:
            yield from self._inorder_generator(node.left)
            yield node
            yield from self._inorder_generator(node.right)

    def _insert(self, new_node: Node):
        parent_node = None
        current_node = self.root

        while current_node is not None:
            parent_node = current_node
            if new_node.key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right

        new_node.parent = parent_node
        if parent_node is None:
            self.root = new_node
        elif new_node.key < parent_node.key:
            parent_node.left = new_node
        else:
            parent_node.right = new_node

        new_node.left = None
        new_node.right = None

    def _transplant(self, x: Node, y: Node):
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        if y is not None:
            y.parent = x.parent

    def _minimum(self, node: Node):
        while node.left is not None:
            node = node.left
        return node

    def _delete(self, target_node: Node):
        if target_node.left is None:
            self._transplant(target_node, target_node.right)

        elif target_node.right is None:
            self._transplant(target_node, target_node.left)

        else:
            min_node = self._minimum(target_node.right)
            min_node_right = min_node.right
            if min_node.parent == target_node:
                min_node_right.parent = target_node

            else:
                self._transplant(min_node, min_node.right)
                min_node.right = target_node.right
                min_node.right.parent = min_node

            self._transplant(target_node, min_node)
            min_node.left = target_node.left
            min_node.left.parent = min_node

    def _find(self, node: Node, key) -> Tuple[Optional[Node], Optional[Node]]:
        if node is None:
            return None, None

        if key == node.key:
            return node, node.parent
        elif key < node.key:
            return self._find(node.left, key)
        else:
            return self._find(node.right, key)

    def get(self, key):
        node, _ = self._find(self.root, key)
        if node is not None:
            return node.value
        return None

    def set(self, key, value):
        node, parent = self._find(self.root, key)
        if node is not None:
            node.value = value
        else:
            node = Node(key, value)
            if parent is None:
                self._insert(node)
            elif key < parent.key:
                parent.left = node
            else:
                parent.right = node
            self.length += 1

    def remove(self, key):
        node, _ = self._find(self.root, key)
        if node is not None:
            self._delete(node)
            self.length -= 1
        return None

    def keys(self):
        for node in self:
            yield node.key

    def values(self):
        for node in self:
            yield node.value

    def items(self):
        for node in self:
            yield node.key, node.value


class Solution:
    def run_commands(self, commands: List[str], arguments: List[Optional[List]]):
        tree_map = None
        commands_output = list()
        for index in range(len(commands)):
            if commands[index] == "TreeMap":
                tree_map = TreeMap()
                commands_output.append(None)
                continue
            if commands[index] == "put":
                commands_output.append(tree_map.set(arguments[index][0], arguments[index][1]))
                continue
            if commands[index] == "remove":
                commands_output.append(tree_map.remove(arguments[index][0]))
                continue
            if commands[index] == "get":
                commands_output.append(tree_map.get(arguments[index][0]))
                continue
        return commands_output
