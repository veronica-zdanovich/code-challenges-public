class BurrowsWheeler:

    def transform(self, input_bytes: bytes) -> bytes:
        i = 0
        transformed_bytearray = bytearray()
        transformed_bytearray.extend(input_bytes)
        transformed_bytes = [input_bytes]
        while i != len(input_bytes) - 1:
            transformed_bytearray = transformed_bytearray[1:] + transformed_bytearray[0].to_bytes()
            transformed_bytes.append(transformed_bytearray)
            i += 1

        sorted_suffixes = sorted(transformed_bytes)
        first = sorted_suffixes.index(input_bytes)
        tails = bytes([suffix[-1] for suffix in sorted_suffixes])

        output_bytes = bytearray()
        output_bytes.extend(first.to_bytes(4, 'little'))
        output_bytes.extend(tails)

        return bytes(output_bytes)

    def inverse_transform(self, input_bytes: bytes) -> bytes:
        first = int.from_bytes(input_bytes[:4], byteorder='little', signed=False)
        tails = [chr(char) for char in input_bytes[4:]]
        first_chars = sorted(tails)

        next_array = [-1 for _ in range(len(first_chars))]
        visited_chars = [False for _ in range(len(first_chars))]

        for i, char in enumerate(first_chars):
            for j, first_char in enumerate(tails):
                if char != first_char or next_array[i] > 0:
                    continue

                if visited_chars[j]:
                    continue

                next_array[i] = j
                visited_chars[j] = True
                break

        next_index = first
        output_bytes = bytearray()

        for _ in first_chars:
            byte = tails[next_array[next_index]]
            output_bytes.extend(byte.encode())
            next_index = next_array[next_index]

        return bytes(output_bytes)
