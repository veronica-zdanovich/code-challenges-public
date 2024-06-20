import unittest

from parameterized import parameterized

from burrowsWheeler.huffmanTransform.huffman import Huffman


class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Huffman()

    @parameterized.expand([
        [b'\x03\x00\x00\x00ARD!RCAAAABB', b'\x01\x01\x00\x00\x01\x01\x00\x03\x00!\x01\x00C\x00D\x01\x01\x00R\x00B\x00A'
                                          b'\n@8\xeb\x1b\xfe\xd0\n\x04'],
        [b'\x04\x00\x00\x00annb$aa', b'\x01\x01\x01\x00\x04\x00$\x00a\x01\x00\x00\x01\x00b\x00n\n\x15?\xe2\xa0\n\x05'],
    ])
    def test_encode(self, input_bytes, output_bytes):
        encoded_bytes = self.solution.encode(input_bytes)
        self.assertEqual(output_bytes, encoded_bytes)

    @parameterized.expand([
        [b'\x01\x01\x00\x00\x01\x00B\x00R\x01\x01\x01\x00C\x00D\x01\x00\x03\x00!\x00A\n\x02\x92\xff\x87r\xf0\n\x04',
         b'\x00\x00\x00\x03BBAAAACR!DRA'],
        [b'\x01\x01\x01\x00\x04\x00$\x00\x00\x01\x00a\x01\x00b\x00n\nTQ\xdf\xc0\n\x05', b'\x00\x00\x00\x04aa$bnna'],
    ])
    def test_decode(self, input_bytes, output_bytes):
        decoded_bytes = self.solution.decode(input_bytes)
        self.assertEqual(output_bytes, decoded_bytes)

