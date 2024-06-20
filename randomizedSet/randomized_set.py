import random
from typing import List, Optional


class RandomizedSet:

    def __init__(self):
        self._inner_map = dict()
        self._inner_list = list()

    def insert(self, val: int) -> bool:
        index = self._inner_map.get(val)
        if index is not None:
            return False

        self._inner_map[val] = len(self._inner_list)
        self._inner_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        index = self._inner_map.get(val)
        if index is None:
            return False

        last_index = len(self._inner_list) - 1
        last_elem = self._inner_list[last_index]
        self._inner_map[last_elem] = index
        self._inner_list[last_index] = val
        self._inner_list[index] = last_elem

        del self._inner_map[val]
        self._inner_list.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self._inner_list)


class Solution:
    def run_commands(self, commands: List[str], arguments: List[Optional[List]]):
        randomized_set = None
        commands_output = list()
        for index in range(len(commands)):
            if commands[index] == "RandomizedSet":
                randomized_set = RandomizedSet()
                commands_output.append(None)
                continue
            if commands[index] == "insert":
                commands_output.append(randomized_set.insert(arguments[index][0]))
                continue
            if commands[index] == "remove":
                commands_output.append(randomized_set.remove(arguments[index][0]))
                continue
            if commands[index] == "getRandom":
                commands_output.append(randomized_set.getRandom())
                continue
        return commands_output


if __name__ == "__main__":
    commands = ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
    args = [[], [1], [2], [2], [], [1], [2], []]
    sol = Solution()
    print(sol.run_commands(commands, args))
