import io
import unittest

from parameterized import parameterized

from printZeroEvenOdd.print_zero_even_odd import Solution


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand([
        [5, "0102030405"],
        [2, "0102"],
        [6, "010203040506"],
        [1, "01"],
    ])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_solution(self, input_n, expected_result, mock_stdout):
        self.solution.run(input_n)
        self.assertEqual(mock_stdout.getvalue(), expected_result)

