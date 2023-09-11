from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def to_list(self, node: Optional[ListNode]) -> Optional[List]:
        result = list()

        while node:
            result.append(node.val)
            node = node.next

        return result

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0

        head = ListNode()
        node = head

        while not (l1 is None and l2 is None and carry == 0):
            first_term = l1.val if l1 is not None else 0
            second_term = l2.val if l2 is not None else 0
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

            temp_sum = first_term + second_term + carry
            carry = temp_sum // 10

            node.next = ListNode(val=temp_sum % 10)
            node = node.next

        return head.next
