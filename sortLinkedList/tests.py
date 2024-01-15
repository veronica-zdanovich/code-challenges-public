import unittest
from typing import Optional, List

from parameterized import parameterized

from addTwoNumbers.add_two_numbers import ListNode
from sortLinkedList.sort_linked_list import Solution


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
        [[4, 2, 3, 1], [1, 2, 3, 4]],
        [[3, 4, 2, 1, 5, 6], [1, 2, 3, 4, 5, 6]],
    ])
    def test_solution(self, nums: List, expected_result: List):
        head = self.fill_in_list_node(nums)
        new_head = self.solution.sortList(head)
        self.assertEqual(self.to_list(new_head), expected_result)


if __name__ == '__main__':
    unittest.main()
