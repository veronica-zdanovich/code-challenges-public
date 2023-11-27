from typing import List


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.back = None
        self._length = 0

    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node
            current_node = current_node.next

    def __len__(self):
        return self._length

    def __repr__(self):
        nodes_repr_list = list()
        current_node = self.head
        if self.head is None:
            nodes_repr_list.append("None")

        while current_node is not None:
            nodes_repr_list.append(str(current_node.value))
            current_node = current_node.next
        return " -> ".join(nodes_repr_list)

    def is_empty(self) -> bool:
        return self.head is None

    def to_list(self) -> List:
        current_node = self.head
        nodes_values = list()
        while current_node is not None:
            nodes_values.append(current_node.value)
            current_node = current_node.next
        return nodes_values

    def push_front(self, value):
        new_head = Node(value)
        self._length += 1
        if self.head is None:
            self.head = new_head
            self.back = self.head
            return

        prev_head = self.head
        self.head = new_head
        new_head.next = prev_head

    def push_back(self, value):
        new_node = Node(value)
        self._length += 1
        if self.head is None:
            self.head = new_node
            self.back = self.head
            return

        self.back.next = new_node
        self.back = new_node

    def insert_after(self, new_value, target_value):
        new_node = Node(new_value)
        self._length += 1
        if self.head is None:
            self.head = new_node
            self.back = self.head
            return

        for current_node in self:
            if current_node.value == target_value:
                new_node.next = current_node.next
                if current_node.next is None:
                    self.back = new_node
                current_node.next = new_node
                return

        raise ValueError

    def insert_before(self, new_value, target_value):
        new_node = Node(new_value)
        self._length += 1
        if self.head is None:
            raise ValueError

        prev_node = self.head
        for current_node in self:
            if current_node.value == target_value:
                prev_node.next = new_node
                new_node.next = current_node
                return
            prev_node = current_node

        raise ValueError

    def pop_front(self):
        if self.head is None:
            raise ValueError

        self.head = self.head.next
        self._length -= 1

    def remove(self, value):
        if self.head is None:
            raise ValueError

        previous_node = self.head
        for current_node in self:
            if current_node.value == value:
                previous_node.next = current_node.next
                self._length -= 1
                if current_node.next is None:
                    self.back = previous_node
                if current_node == self.head:
                    self.head = current_node.next
                return
            previous_node = current_node
        raise ValueError

    def pop_back(self):
        if self.head is None:
            raise ValueError

        previous_node = self.head
        for current_node in self:
            if current_node.next is None:
                self._length -= 1
                previous_node.next = None
                self.back = previous_node
                return
            previous_node = current_node

    def find_value(self, value):
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return current_node
            current_node = current_node.next
        return None

    def reverse(self):
        prev_node = None
        current_node = self.head
        self.back = current_node

        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        self.head = prev_node

