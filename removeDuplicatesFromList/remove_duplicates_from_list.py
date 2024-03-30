from typing import List


# Given an array of integers, the task is to remove the duplicates from the array.

#

# Example:

#

# Original list is: [1, 5, 3, 6, 3, 5, 6, 1]

# List after removing duplicates: [1, 5, 3, 6]

class Solution:
    def remove_duplicates(self, original_list: List[int]) -> List[int]:
        if len(original_list) < 2:
            return original_list

        visited_digits_set = set()
        index = 0

        while index < len(original_list):
            item = original_list[index]
            if item in visited_digits_set:
                last_elem = original_list[-1]
                last_index = len(original_list) - 1

                original_list[index] = last_elem
                original_list[last_index] = item

                original_list.pop()
            else:
                visited_digits_set.add(item)
                index += 1

        return original_list
