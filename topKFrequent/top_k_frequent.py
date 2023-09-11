import collections
from typing import List

from binaryHeap.binary_heap import BinaryHeap


class PriorityItem:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

    def __gt__(self, other):
        return self.priority > other.priority

    def __lt__(self, other):
        return self.priority < other.priority


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:  # O(N*log(k))
        occurrences_dict = collections.Counter(nums)  # O(N)
        binary_heap = BinaryHeap()

        for num, occurrence in occurrences_dict.items():  # O(N)
            element = PriorityItem(num, occurrence)
            if len(binary_heap) < k:
                binary_heap.push(element)  # O(log(k)
                continue

            if len(binary_heap) == k:
                root_element = binary_heap.get_root()  # O(1)
                if root_element < element:
                    binary_heap.replace_root(element)  # O(log(k)

        return [item.value for item in binary_heap.list_items()]
