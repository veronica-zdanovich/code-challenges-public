import unittest

from parameterized import parameterized

from minimumGeneticMutation.minimum_genetic_mutation import Solution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand([
        ["AACCGGTT", "AACCGGTA", ["AACCGGTA"], 1],
        ["AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"], 2],
        ["AACCGGTT", "AACCGCTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"], 2],
        ["AAAAACCC", "AACCCCCC", ["AAAACCCC", "AAACCCCC", "AACCCCCC"], 3],
        ["AACCGGTT", "AAACGGTA", ["AACCGATT", "AACCGATA", "AAACGATA", "AAACGGTA"], 4],
        ])
    def test_solution(self, start_gene, end_gene, bank, expected_result):
        self.assertEqual(expected_result, self.solution.minMutation(start_gene, end_gene, bank))
