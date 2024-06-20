import unittest

from faker import Faker

from burrowsWheeler.compression import CompressionAlgorithm


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = CompressionAlgorithm()
        self.fake = Faker()

    def test_compression(self):
        for _ in range(10):
            input_str = self.fake.pystr()
            input_bytes = input_str.encode('utf-8')

            encoded = self.solution.compress(input_bytes)
            decoded = self.solution.decompress(encoded)

            output_str = decoded.decode('utf-8')
            self.assertEqual(input_str, output_str)
