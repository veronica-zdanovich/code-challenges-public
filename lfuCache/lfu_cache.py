from typing import List, Optional


class Node:
    def __init__(self, key: int = None, value: int = None, frequency: int = None):
        self.value = value
        self.key = key
        self.frequency = frequency

        self.parent = None
        self.next = None


class LinkedList(Node):
    def __init__(self, value: int = None):
        super().__init__()
        self.length = 0
        self.head = Node(value=value)
        self.tail = Node()
        self.tail.parent = self.head
        self.head.next = self.tail

    def popleft(self) -> Node:
        node = self.head.next
        self.head.next = node.next
        node.next.parent = self.head
        self.length -= 1

        return node

    def appendleft(self, node: Node):
        self.head.next.parent = node
        node.parent = self.head
        node.next = self.head.next
        self.head.next = node

        self.length += 1

    def append(self, node):
        node.parent = self.tail.parent
        self.tail.parent.next = node
        node.next = self.tail
        self.tail.parent = node

        self.length += 1

    def remove_node(self, node):
        node.parent.next = node.next
        node.next.parent = node.parent

        self.length -= 1


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_node = dict()
        self.frequency_section = dict()

        self.sections = LinkedList()

    def _move_to_next_section(self, key: int):
        section = self._get_section(self.key_node[key].frequency)
        section.remove_node(self.key_node[key])

        new_frequency = self.key_node[key].frequency + 1
        self.key_node[key].frequency = new_frequency

        next_section = self._get_section(new_frequency)
        next_section.append(self.key_node[key])

        if self.frequency_section.get(new_frequency) is None:
            self._insert_section(new_frequency, section, next_section)

        if section.length == 0:
            self._remove_empty_section(section)

    def _get_section(self, frequency: int) -> [Node, LinkedList]:
        if self.frequency_section.get(frequency) is None:
            return LinkedList(value=frequency)
        return self.frequency_section[frequency]

    def _insert_section(self, frequency: int, section: Node, next_section: Node = None):
        if next_section is None:
            self.frequency_section[frequency] = section
            self.sections.appendleft(section)
        else:
            self.frequency_section[frequency] = next_section
            next_section.parent = section
            next_section.next = section.next
            section.next = next_section

    def _remove_empty_section(self, section):
        del self.frequency_section[section.head.value]
        self.sections.remove_node(section)

    def _pop_least_frequent(self):
        if len(self.key_node) < self.capacity:
            return

        least_frequent_section = self.sections.head.next
        least_frequent = least_frequent_section.popleft()
        del self.key_node[least_frequent.key]

        if least_frequent_section.length == 0:
            self._remove_empty_section(least_frequent_section)

    def get(self, key: int) -> int:
        if self.key_node.get(key) is None:
            return -1

        self._move_to_next_section(key)
        return self.key_node[key].value

    def put(self, key: int, value: int) -> None:
        if self.key_node.get(key) is None:
            self._pop_least_frequent()

            section = self._get_section(frequency=1)
            if self.frequency_section.get(1) is None:
                self._insert_section(1, section)

            self.key_node[key] = Node(key, value, 1)
            section.append(self.key_node[key])
        else:
            self._move_to_next_section(key)
            self.key_node[key].value = value


class Solution:
    def run_commands(self, commands: List[str], arguments: List[Optional[List]]):
        cache = None
        commands_output = list()
        for index in range(len(commands)):
            if commands[index] == "LFUCache":
                cache = LFUCache(arguments[index][0])
                commands_output.append(None)
                continue
            if commands[index] == "put":
                cache.put(arguments[index][0], arguments[index][1])
                commands_output.append(None)
                continue
            if commands[index] == "get":
                commands_output.append(cache.get(arguments[index][0]))
                continue
        return commands_output
