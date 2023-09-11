from copy import copy


class BinaryHeap:
    def __init__(self):
        self.items = list()

    def __len__(self):
        return len(self.items)

    def _sift_up(self, index: int):
        parent_index = (index - 1) // 2

        while index > 0 and self.items[parent_index] > self.items[index]:
            self._swap(index, parent_index)
            index = parent_index
            parent_index = (index - 1) // 2

    def _sift_down(self, index: int):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest = index

        if left_child_index < len(self.items) and self.items[smallest] > self.items[left_child_index]:
            smallest = left_child_index

        if right_child_index < len(self.items) and self.items[smallest] > self.items[right_child_index]:
            smallest = right_child_index

        if smallest != index:
            self._swap(index, smallest)
            self._sift_down(smallest)

    def _swap(self, left_index: int, right_index: int):
        self.items[left_index], self.items[right_index] = self.items[right_index], self.items[left_index]

    def _last_index(self) -> int:
        return len(self.items) - 1

    def push(self, element):
        self.items.append(element)
        self._sift_up(self._last_index())

    def pop(self):
        if not self.items:
            return None

        min_element = self.items[0]
        last_element = self.items.pop()

        if self.items:
            self.items[0] = last_element
            self._sift_down(0)

        return min_element

    def get_root(self) -> int:
        return self.items[0]

    def list_items(self) -> list:
        return copy(self.items)

    def replace_root(self, item):
        if not self.items:
            return None

        if self.items:
            self.items[0] = item
            self._sift_down(0)
