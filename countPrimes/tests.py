import unittest

from parameterized import parameterized

from countPrimes.count_primes import Solution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand([
        [10, 4],
        [2, 0],
        [1, 0],
        [3, 1],
        [499979, 41537],
        [999983, 78497],
        ])
    def test_solution(self, n, expected_result):
        self.assertEqual(expected_result, self.solution.countPrimes(n))
