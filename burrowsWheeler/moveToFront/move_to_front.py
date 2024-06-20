class MoveToFront:

    def encode(self, input_bytes: bytes) -> bytes:
        first = int.from_bytes(bytes(input_bytes[:4]), byteorder='little', signed=False)
        tails = input_bytes[4:]

        alphabet = [chr(i) for i in range(256)]
        encoded = list()
        for index in tails:
            char = chr(index)
            encoded.insert(0, index)
            alphabet.pop(index)
            alphabet.insert(0, char)

        output_bytes = bytearray()
        output_bytes.extend(first.to_bytes(4, 'little'))
        output_bytes.extend(bytes(encoded))

        return bytes(output_bytes)

    def decode(self, input_bytes: bytes) -> bytes:
        first = input_bytes[:4]

        alphabet = [chr(i) for i in range(256)]
        decoded = list()
        for num in input_bytes[4:]:
            char = chr(num)
            decoded.insert(0, char)
            alphabet.pop(num)
            alphabet.insert(0, char)

        output_bytes = first + bytes([ord(i) for i in decoded])
        return output_bytes
