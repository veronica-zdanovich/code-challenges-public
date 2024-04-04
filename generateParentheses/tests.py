import unittest

from parameterized import parameterized

from generateParentheses.generate_parentheses import Solution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand([
        [3, ['((()))', '(()())', '(())()', '()(())', '()()()']],
        [1, ['()']],
        [2, ['(())', '()()']],
    ])
    def test_solution(self, n, expected_result):
        self.assertEqual(expected_result, self.solution.generateParenthesis(n))
