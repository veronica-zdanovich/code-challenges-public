import unittest

from parameterized import parameterized

from mergeIntervals.merge_intervals import Solution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand([
        [[[2, 6], [1, 3], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]],
        [[[1, 4], [4, 5]], [[1, 5]]],
        [[[1, 3]], [[1, 3]]],
        [[[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]],
        [[[1, 4], [0, 2], [3, 5]], [[0, 5]]],
    ])
    def test_solution(self, intervals, expected_result):
        self.assertEqual(expected_result, self.solution.merge(intervals))


if __name__ == '__main__':
    unittest.main()
