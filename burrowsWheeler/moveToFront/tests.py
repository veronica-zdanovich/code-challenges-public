import unittest

from parameterized import parameterized

from burrowsWheeler.moveToFront.move_to_front import MoveToFront


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = MoveToFront()

    @parameterized.expand([
        [b'\x03\x00\x00\x00ARD!RCAAAABB', b'\x03\x00\x00\x00BBAAAACR!DRA'],
        [b'\x04\x00\x00\x00annb$aa', b'\x04\x00\x00\x00aa$bnna'],
    ])
    def test_encode(self, input_bytes, output_bytes):
        self.assertEqual(output_bytes, self.solution.encode(input_bytes))

    @parameterized.expand([
        [b'\x03\x00\x00\x00BBAAAACR!DRA', b'\x03\x00\x00\x00ARD!RCAAAABB'],
        [b'\x04\x00\x00\x00aa$bnna', b'\x04\x00\x00\x00annb$aa'],
    ])
    def test_decode(self, input_bytes, output_bytes):
        self.assertEqual(output_bytes, self.solution.decode(input_bytes))
