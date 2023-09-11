import unittest
from typing import List, Optional

from parameterized import parameterized

from addTwoNumbers.add_two_numbers import ListNode, Solution


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

    @parameterized.expand([
        [[2, 4, 3], [5, 6, 4], [7, 0, 8]],
        [[0], [0], [0]],
        [[9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]],
        [None, None, []],
    ])
    def test_solution(self, input_list_1: List, input_list_2: List, expected_result: List):
        l1 = self.fill_in_list_node(input_list_1)
        l2 = self.fill_in_list_node(input_list_2)

        result_node = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(self.solution.to_list(result_node), expected_result)


if __name__ == '__main__':
    unittest.main()
