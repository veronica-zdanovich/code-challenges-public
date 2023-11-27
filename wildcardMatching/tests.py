import unittest

from parameterized import parameterized

from wildcardMatching.wildcard_matching import Solution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand([
        ["aa", "a", False],
        ["aa", "aa", True],
        ["a", "a", True],
        ["aa", "*", True],
        ["", "****", True],
        ["aab", "c*a*b", False],
        ["abcabcde", "*abc???de*", True],
        ["", "", True],
        ["", "?", False],
        ["adceb", "*a*b", True],
        ["mississippi", "m??*ss*?i*pi", False],
        ["acdcb", "a*c?b", False],
        ["abcabczzzde", "*abc???de*", True],
        ["c", "*?*", True],
        ["ab", "*a", False],
        ["", "*a*", False],
        ])
    def test_solution(self, s, p, expected_result):
        self.assertEqual(expected_result, self.solution.isMatch(s, p))
