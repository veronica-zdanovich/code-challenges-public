import unittest

from parameterized import parameterized

from topKFrequent.top_k_frequent import Solution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand([
        [[5, -3, 9, 1, 7, 7, 9, 10, 2, 2, 10, 10, 3, -1, 3, 7, -9, -1, 3, 3], 3, [7, 3, 10]],
        [[1, 1, 1, 2, 2, 3], 2, [2, 1]],
        [[1], 1, [1]],
        [[3, 0, 1, 0], 1, [0]],
        [[5, 2, 5, 3, 5, 3, 1, 1, 3], 2, [3, 5]],
        [[4, 1, -1, 2, -1, 2, 3], 2, [2, -1]],
    ])
    def test_solution(self, input_array, k, expected_result):
        self.assertEqual(self.solution.topKFrequent(input_array, k), expected_result)


if __name__ == '__main__':
    unittest.main()
