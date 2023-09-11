class Node:
    def __init__(self, is_end=False):
        self.children = dict()
        self.is_end = is_end


class Trie:

    def __init__(self):
        self.head = Node()
        self.head.children[""] = dict()

    def _add_node(self, char: str, current_node: Node) -> Node:
        node = Node()
        current_node.children[char] = node
        return node

    def insert(self, word: str) -> None:
        current_node = self.head

        for char in word:
            next_node = current_node.children.get(char)
            if next_node:
                current_node = next_node
            else:
                current_node = self._add_node(char, current_node)
        current_node.is_end = True

    def search(self, word: str) -> bool:
        current_node = self.head

        for char in word:
            next_node = current_node.children.get(char)
            if not next_node:
                return False

            current_node = next_node
        return current_node.is_end

    def startsWith(self, prefix: str) -> bool:
        current_node = self.head

        for char in prefix:
            next_node = current_node.children.get(char)
            if not next_node:
                return False

            current_node = next_node
        return True


class Solution:
    def __init__(self):
        self.commands_output = list()

    def run_commands(self, commands, arguments):
        trie = None
        for index in range(len(commands)):
            if commands[index] == "Trie":
                trie = Trie()
                self.commands_output.append(None)
                continue
            if commands[index] == "insert":
                self.commands_output.append(trie.insert(arguments[index][0]))
                continue
            if commands[index] == "search":
                self.commands_output.append(trie.search(arguments[index][0]))
                continue
            if commands[index] == "startsWith":
                self.commands_output.append(trie.startsWith(arguments[index][0]))
                continue

    def show_output(self):
        return self.commands_output
