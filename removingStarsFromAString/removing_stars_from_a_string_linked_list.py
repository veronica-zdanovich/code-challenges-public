class Node:
    def __init__(self, value: str, parent=None, next=None):
        self.value = value
        self.next = next
        self.parent = parent


class Solution:
    def removeStars(self, s: str) -> str:
        if len(s) == 0:
            return s

        head = Node("")
        current_node = head
        for char in s:
            if char == "*":
                current_node = current_node.parent
                current_node.next = None
            else:
                new_node = Node(char, parent=current_node)
                current_node.next = new_node
                current_node = new_node

        current_node = head.next
        non_star_list = list()
        while current_node is not None:
            non_star_list.append(current_node.value)
            current_node = current_node.next

        return "".join(non_star_list)
