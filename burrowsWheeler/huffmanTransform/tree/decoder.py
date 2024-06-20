class Node:
    def __init__(self, value: int = None):
        self.value = value
        self.right = None
        self.left = None


def fill_in_tree(symbols, visited, i):
    if len(symbols) == i:
        return

    while visited[i] is True:
        i += 1
        if i == len(symbols):
            return

    visited[i] = True
    node = None
    if symbols[i] == 1:
        node = Node()
        node.left = fill_in_tree(symbols, visited, i + 1)
        node.right = fill_in_tree(symbols, visited, i + 1)
    elif symbols[i] == 0:
        value = symbols[i + 1]
        node = Node(value)
        visited[i + 1] = True

    return node


def read_tree(symbols: bytes):
    visited = [False for _ in range(len(symbols))]
    root = fill_in_tree(list(symbols), visited, 0)
    return root
