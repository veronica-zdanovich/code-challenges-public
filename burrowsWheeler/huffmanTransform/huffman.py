from collections import Counter
from queue import PriorityQueue

import bitstring

from burrowsWheeler.huffmanTransform.tree.decoder import read_tree
from burrowsWheeler.huffmanTransform.tree.encoder import dump_tree


class Node:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.right = None
        self.left = None

    def __eq__(self, other):
        return self.key == other.key

    def __gt__(self, other):
        return self.key > other.key

    def __lt__(self, other):
        return self.key < other.key

    def __repr__(self):
        return f"{self.key}: {self.value}"


class Huffman:
    def _fill_codes(self, current_node: Node, code: str, codes_map: dict):
        if current_node is None:
            return

        if current_node.value is not None:
            codes_map[current_node.value] = code
            return

        self._fill_codes(current_node.left, code + "0", codes_map)
        self._fill_codes(current_node.right, code + "1", codes_map)

    def _appended_zeros(self, code_len: int) -> int:
        return 8 * ((code_len + 7) // 8) - code_len

    def _cut_tailing_zeroes(self, binary_string: str, appended_zeroes: int) -> str:
        return binary_string[:len(binary_string) - appended_zeroes]

    def encode(self, input_bytes: bytes) -> bytes:
        repetitions = Counter(input_bytes)
        min_heap = PriorityQueue()

        for key, repetition in repetitions.items():
            min_heap.put(item=Node(repetition, int(key)))

        parent = None
        while min_heap.qsize() > 1:
            left = min_heap.get()
            right = min_heap.get()

            parent = Node(left.key + right.key)
            parent.left = left
            parent.right = right
            min_heap.put(item=parent)

        current_node = parent
        current_code = ""

        codes_map = dict()
        self._fill_codes(current_node, current_code, codes_map)

        bit_string = str()

        for byte in input_bytes:
            code = codes_map[byte]
            bit_string += code

        is_bin_string_extended = False

        appended_zeros = self._appended_zeros(len(bit_string))
        if len(bit_string) // 8 != 0:
            bit_string = bit_string + "0" * appended_zeros
            is_bin_string_extended = True

        bit_array = bitstring.BitArray(bin=bit_string)
        encoded_input_bytes = bit_array.tobytes()

        tree_bytes = bytearray()
        dump_tree(parent, tree_bytes)

        output_bytes = bytearray()
        output_bytes.extend(tree_bytes)
        output_bytes.extend(b"\n")
        output_bytes.extend(encoded_input_bytes)

        if is_bin_string_extended:
            output_bytes.extend(b"\n")
            output_bytes.extend(appended_zeros.to_bytes(1, 'little'))

        return bytes(output_bytes)

    def decode(self, input_bytes: bytes) -> bytes:
        input_bytes = input_bytes.split(b"\n")

        is_bin_string_extended = False
        tree, *encoded_bytes = input_bytes

        if len(encoded_bytes[-1]) == 1:
            is_bin_string_extended = True
            appended_zeroes = int.from_bytes(encoded_bytes[-1], "little")
            encoded_bytes.pop()
            encoded_bytes = b'\n'.join(encoded_bytes)

        read_bit_array = bitstring.BitArray(encoded_bytes)
        binary_string = read_bit_array.bin
        if is_bin_string_extended:
            binary_string = self._cut_tailing_zeroes(binary_string, appended_zeroes)

        root = read_tree(tree)
        current_node = root

        i = 0
        output_bytes = bytearray()
        while i < len(binary_string):
            bit = binary_string[i]

            if bit == "0":
                temp = current_node.left
                if temp is not None:
                    current_node = temp
            elif bit == "1":
                temp = current_node.right
                if temp is not None:
                    current_node = temp

            if current_node.value is not None:
                output_bytes.append(current_node.value)
                current_node = root

            i += 1

        return bytes(output_bytes)
