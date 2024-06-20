ZERO_BYTE = (0).to_bytes(1, 'little')
ONE_BYTE = (1).to_bytes(1, 'little')


def get_byte_length(i: int) -> int:
    return max((i.bit_length() + 7) // 8, 1)


def dump_tree(tree, buffer: bytearray):
    if tree.value is None:  # Node
        buffer.extend(ONE_BYTE)
        dump_tree(tree.left, buffer)
        dump_tree(tree.right, buffer)
    else:  # Leaf
        buffer.extend(ZERO_BYTE)
        bytes_len = get_byte_length(tree.value)
        buffer.extend(tree.value.to_bytes(bytes_len, 'little'))
