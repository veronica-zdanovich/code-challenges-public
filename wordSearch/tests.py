import unittest

from parameterized import parameterized

from wordSearch.word_search import Solution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand([
        [[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED", True],
        [[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE", True],
        [[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB", False],
        [[["a", "b"]], "ba", True],
        [[["a", "a"]], "aaa", False],
        [[["a", "b"], ["c", "d"]], "acdb", True],
        ])
    def test_solution(self, board, word, expected_result):
        self.assertEqual(expected_result, self.solution.exist(board, word))
