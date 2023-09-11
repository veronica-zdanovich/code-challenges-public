import unittest

from sortColors.sort_colors import Solution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        arr = [2, 0, 2, 1, 1, 0]
        expected_result = [0, 0, 1, 1, 2, 2]
        self.solution.sort_colors(arr)
        self.assertEqual(expected_result, arr)

    def test_2(self):
        arr = [2, 0, 1]
        expected_result = [0, 1, 2]
        self.solution.sort_colors(arr)
        self.assertEqual(expected_result, arr)

    def test_3(self):
        arr = [1]
        expected_result = [1]
        self.solution.sort_colors(arr)
        self.assertEqual(expected_result, arr)

    def test_4(self):
        arr = [1, 1, 0]
        expected_result = [0, 1, 1]
        self.solution.sort_colors(arr)
        self.assertEqual(expected_result, arr)


if __name__ == '__main__':
    unittest.main()
