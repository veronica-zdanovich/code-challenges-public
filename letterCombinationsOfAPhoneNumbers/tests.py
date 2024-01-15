import unittest

from parameterized import parameterized

from letterCombinationsOfAPhoneNumbers.letter_combinations_of_a_phone_number import Solution
from letterCombinationsOfAPhoneNumbers.letter_combinations_of_a_phone_numbers_backtracking import Solution as SolutionBacktracking


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.solution_backtracking = SolutionBacktracking()

    @parameterized.expand([
        ["23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]],
        ["234", ["adg", "adh", "adi", "aeg", "aeh", "aei", "afg", "afh", "afi", "bdg", "bdh", "bdi", "beg", "beh",
                 "bei", "bfg", "bfh", "bfi", "cdg", "cdh", "cdi", "ceg", "ceh", "cei", "cfg", "cfh", "cfi"]],
    ])
    def test_solution(self, number, expected_result):
        self.assertEqual(expected_result, self.solution.letterCombinations(number))
        self.assertEqual(expected_result, self.solution_backtracking.letterCombinations(number))


if __name__ == "__main__":
    unittest.main()
