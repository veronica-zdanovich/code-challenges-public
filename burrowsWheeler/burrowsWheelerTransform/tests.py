import unittest

from parameterized import parameterized

from burrowsWheeler.burrowsWheelerTransform.burrows_wheeler import BurrowsWheeler


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = BurrowsWheeler()

    @parameterized.expand([
        [b'ABRACADABRA!', b'\x03\x00\x00\x00ARD!RCAAAABB'],
        [b'banana$', b'\x04\x00\x00\x00annb$aa'],
        ])
    def test_transform(self, input_str, output_bytes):
        self.assertEqual(output_bytes, self.solution.transform(input_str))

    @parameterized.expand([
        [b'\x03\x00\x00\x00ARD!RCAAAABB', b'ABRACADABRA!'],
        [b'\x04\x00\x00\x00annb$aa', b'banana$'],
        ])
    def test_inverse_transform(self, input_bytes, output_bytes):
        self.assertEqual(output_bytes, self.solution.inverse_transform(input_bytes))
