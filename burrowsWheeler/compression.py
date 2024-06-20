from burrowsWheeler.burrowsWheelerTransform.burrows_wheeler import BurrowsWheeler
from burrowsWheeler.huffmanTransform.huffman import Huffman
from burrowsWheeler.moveToFront.move_to_front import MoveToFront


class CompressionAlgorithm:
    def __init__(self):
        self.huffman = Huffman()
        self.move_to_front = MoveToFront()
        self.burrows_wheeler = BurrowsWheeler()

    def compress(self, data: bytes) -> bytes:
        bwt = self.burrows_wheeler.transform(data)
        mft = self.move_to_front.encode(bwt)
        ht = self.huffman.encode(mft)
        return ht

    def decompress(self, data: bytes) -> bytes:
        ht = self.huffman.decode(data)
        mtf = self.move_to_front.decode(ht)
        bwt = self.burrows_wheeler.inverse_transform(mtf)
        return bwt


if __name__ == "__main__":
    compression_algorithm = CompressionAlgorithm()

    with open("abra.txt", "rb") as file:
        input_data = file.read()
        print(f"Original size: {file.tell()}")

    encoded = compression_algorithm.compress(input_data)

    with open("abra.txt", "wb") as file:
        file.write(encoded)
        print(f"Compressed size: {file.tell()}")

    decoded = compression_algorithm.decompress(encoded)

    with open("abra.txt", "w") as file:
        file.write(decoded.decode("utf-8"))
        print(f"Original size: {file.tell()}")
