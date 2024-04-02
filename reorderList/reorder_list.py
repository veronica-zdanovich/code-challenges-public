from collections import deque
from typing import Optional

from addTwoNumbers.add_two_numbers import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        current_node = head
        double_ended_queue = deque()
        while current_node is not None:
            double_ended_queue.append(current_node.val)
            current_node = current_node.next

        current_node = head
        counter = 0
        while current_node is not None:
            if counter % 2 == 0:
                current_node.val = double_ended_queue.popleft()
            else:
                current_node.val = double_ended_queue.pop()
            current_node = current_node.next
            counter += 1
