import unittest

from parameterized import parameterized

from repeatedDNASequence.repeated_dna_sequence import Solution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand([
        ["AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT", ["CCCCCAAAAA", "AAAAACCCCC"]],
        ["AAAAAAAAAAAAA", ["AAAAAAAAAA"]],
        [[], []],
        ["AAAAAGCCCCCAAAAGACCCCCCAAAAAGGGTTT", []],
    ])
    def test_solution(self, input_str, expected_result):
        self.assertCountEqual(expected_result, self.solution.findRepeatedDnaSequences(input_str))
