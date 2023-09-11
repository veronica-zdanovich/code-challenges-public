import unittest

from parameterized import parameterized

from validParentheses.valid_parentheses import Solution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand([
        ["{[]}", True],
        ["{}()[]", True],
        ["{[", False],
        ["{", False],
        ["{]", False],
    ])
    def test_solution(self, input_array, expected_result):
        self.assertEqual(self.solution.isValid(input_array), expected_result)


if __name__ == '__main__':
    unittest.main()
