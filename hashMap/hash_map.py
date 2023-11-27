from typing import List, Optional


from linkedList.linked_list import LinkedList


class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __eq__(self, target):
        return self.key == target

    def __str__(self):
        return f'{self.key}:  {self.value}'


class MyHashMap:
    def __init__(self, size=16, load_factor_threshold=0.7):
        self.buckets = [LinkedList() for _ in range(size)]
        self.load_factor_threshold = load_factor_threshold
        self.count = 0

    def __delitem__(self, key):
        self.remove(key)

    def __getitem__(self, key) -> Optional[int]:
        index = self._hash(key)
        node = self.buckets[index].find_value(key)
        if node is not None:
            return node.value.value
        return None

    def __setitem__(self, key, value):
        self.set(key, value)

    def _hash(self, key, size=None):
        if size is None:
            size = len(self.buckets)

        hash_value = 0
        key_str = str(key)
        for char in key_str:
            hash_value = (hash_value * 33 + ord(char)) % size
        return hash_value

    def _resize(self):
        new_size = int(len(self.buckets) * 1.5)
        new_buckets = [LinkedList() for _ in range(new_size)]

        for bucket in self.buckets:
            for node in bucket:
                entry = node.value
                index = self._hash(entry.key, new_size)
                new_buckets[index].push_back(entry)

        self.buckets = new_buckets

    def set(self, key: int, value: int) -> None:
        load_factor = self.count / len(self.buckets)
        if load_factor > self.load_factor_threshold:
            self._resize()

        index = self._hash(key)
        new_entry = Entry(key, value)
        node = self.buckets[index].find_value(key)
        if node is None:
            self.buckets[index].push_back(new_entry)
            self.count += 1
        else:
            node.value = new_entry

    def get(self, key: int) -> Optional[int]:
        index = self._hash(key)
        node = self.buckets[index].find_value(key)
        if node is not None:
            return node.value.value
        return None

    def remove(self, key: int):
        index = self._hash(key)
        try:
            self.buckets[index].remove(key)
        except ValueError:
            pass

    def keys(self):
        for bucket in self.buckets:
            for node in bucket:
                yield node.value.key

    def values(self):
        for bucket in self.buckets:
            for node in bucket:
                yield node.value.value

    def items(self):
        for bucket in self.buckets:
            for node in bucket:
                yield node.value.key, node.value.value

    def __len__(self):
        length = 0
        for bucket in self.buckets:
            length += len(bucket)
        return length


class Solution:
    def run_commands(self, commands: List[str], arguments: List[Optional[List]]):
        hashmap = None
        commands_output = list()
        for index in range(len(commands)):
            if commands[index] == "MyHashMap":
                hashmap = MyHashMap()
                commands_output.append(None)
                continue
            if commands[index] == "put":
                commands_output.append(hashmap.set(arguments[index][0], arguments[index][1]))
                continue
            if commands[index] == "remove":
                commands_output.append(hashmap.remove(arguments[index][0]))
                continue
            if commands[index] == "get":
                commands_output.append(hashmap.get(arguments[index][0]))
                continue
        return commands_output

