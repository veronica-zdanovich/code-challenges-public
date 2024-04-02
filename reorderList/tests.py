import unittest
from typing import Optional, List

from parameterized import parameterized

from addTwoNumbers.add_two_numbers import ListNode
from reorderList.reorder_list import Solution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def fill_in_list_node(self, values: Optional[List]) -> Optional[ListNode]:
        if values is None:
            return None

        head = ListNode()
        node = head
        for value in values:
            node.next = ListNode(value)
            node = node.next
        return head.next

    def to_list(self, node: Optional[ListNode]) -> Optional[List]:
        result = list()

        while node:
            result.append(node.val)
            node = node.next

        return result

    @parameterized.expand([
        [[1, 5, 3, 6, 3, 5, 6, 1], [1, 1, 5, 6, 3, 5, 6, 3]],
        [[1, 2, 3, 4], [1, 4, 2, 3]],
        [[1, 2, 3, 4, 5], [1, 5, 2, 4, 3]],
        [[1, 2, 3, 2, 1], [1, 1, 2, 2, 3]],
        ])
    def test_solution(self, input_list, expected_result):
        head = self.fill_in_list_node(input_list)
        self.solution.reorderList(head)
        self.assertEqual(expected_result, self.to_list(head))
