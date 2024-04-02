import unittest

from parameterized import parameterized

from removingStarsFromAString.removing_stars_from_a_string_stack import Solution as StackSolution
from removingStarsFromAString.removing_stars_from_a_string_linked_list import Solution as LinkedListSolution


class Tests(unittest.TestCase):
    def setUp(self):
        self.stack_solution = StackSolution()
        self.linked_list_solution = LinkedListSolution()

    @parameterized.expand([
        ["leet**cod*e", "lecoe"],
        ["erase*****", ""],
        ])
    def test_solution(self, input_str, expected_result):
        self.assertEqual(expected_result, self.stack_solution.removeStars(input_str))
        self.assertEqual(expected_result, self.linked_list_solution.removeStars(input_str))
