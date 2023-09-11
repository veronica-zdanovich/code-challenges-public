import unittest
from implementTrie.trie import Solution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        commands = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
        args = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
        expected_result = [None, None, True, False, True, None, True]
        self.solution.run_commands(commands, args)
        self.assertEqual(self.solution.show_output(), expected_result)

    def test_2(self):
        commands = ["Trie", "startsWith"]
        args = [[], ["a"]]
        expected_result = [None, False]
        self.solution.run_commands(commands, args)
        self.assertEqual(self.solution.show_output(), expected_result)

    def test_3(self):
        commands = ["Trie", "insert", "startsWith"]
        args = [[], ["hotdog"], ["dog"]]
        expected_result = [None, None, False]
        self.solution.run_commands(commands, args)
        self.assertEqual(self.solution.show_output(), expected_result)

    def test_4(self):
        commands = ["Trie", "insert", "insert", "insert", "insert", "insert", "insert", "search", "search", "search",
                    "search", "search", "search", "search", "search", "search", "startsWith", "startsWith",
                    "startsWith", "startsWith", "startsWith", "startsWith", "startsWith", "startsWith", "startsWith"]
        args = [[], ["app"], ["apple"], ["beer"], ["add"], ["jam"], ["rental"], ["apps"], ["app"], ["ad"],
                     ["applepie"], ["rest"], ["jan"], ["rent"], ["beer"], ["jam"], ["apps"], ["app"], ["ad"],
                     ["applepie"], ["rest"], ["jan"], ["rent"], ["beer"], ["jam"]]
        expected_result = [None, None, None, None, None, None, None, False, True, False, False, False, False, False,
                           True, True, False, True, True, False, False, False, True, True, True]
        self.solution.run_commands(commands, args)
        self.assertEqual(self.solution.show_output(), expected_result)


if __name__ == '__main__':
    unittest.main()
