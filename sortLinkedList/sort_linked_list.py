from typing import Optional, List

from addTwoNumbers.add_two_numbers import ListNode


class Solution:
    def merge_sort(self, nums: List[int]):
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2

        left_part = self.merge_sort(nums[:mid])
        right_part = self.merge_sort(nums[mid:])
        return self.merge(left_part, right_part)

    def merge(self, left_arr: List[int], right_arr: List[int]):
        result = list()
        i = j = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                result.append(left_arr[i])
                i += 1
            else:
                result.append(right_arr[j])
                j += 1

        result.extend(left_arr[i:])
        result.extend(right_arr[j:])
        return result

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        current_node = head
        array = list()
        while current_node is not None:
            array.append(current_node.val)
            current_node = current_node.next

        array = self.merge_sort(array)

        i = 0
        current_node = head
        while current_node is not None and i < len(array):
            current_node.val = array[i]
            current_node = current_node.next
            i += 1
        return head
