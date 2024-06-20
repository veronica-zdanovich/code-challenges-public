import unittest

from parameterized import parameterized

from groupConveyor.conveyor import Conveyor


class Tests(unittest.TestCase):
    @parameterized.expand([
        [[1, 1, 5, 8, 7], 3, [[], [], [], [], [5, 7, 8]]],
        [[5, 7, 7, 8, 8, 10], 3, [[], [], [5, 7, 7], [], [], [8, 8, 10]]],
        [[0, 0, 0, 0, 0, 7], 3, [[], [], [0, 0, 0], [], [], []]]
        ])
    def test_solution(self, stream, distance, expected_result):
        self.conveyor = Conveyor(distance)
        for i in range(len(stream)):
            self.assertEqual(expected_result[i], self.conveyor.add_value(stream[i]))
