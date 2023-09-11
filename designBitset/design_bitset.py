class Bitset:

    def __init__(self, size: int):
        self.num = 0
        self.sum = 0
        self.size = size

    def fix(self, idx: int) -> None:
        xor_mask = self._get_xor_mask(idx)
        bit_offset = self.size - idx - 1
        if (self.num >> bit_offset) % 2 == 0:
            if self.sum < self.size:
                self.sum += 1
            self.num = self.num ^ xor_mask

    def unfix(self, idx: int) -> None:
        xor_mask = self._get_xor_mask(idx)
        bit_offset = self.size - idx - 1
        if xor_mask <= self.num and (self.num >> bit_offset) % 2 == 1:
            if self.sum > 0:
                self.sum -= 1
            self.num = self.num ^ xor_mask

    def flip(self) -> None:
        self.num = self.num ^ self._get_full_bitset()
        self.sum = self.size - self.sum

    def all(self) -> bool:
        return self.sum == self.size

    def one(self) -> bool:
        return self.sum >= 1

    def count(self) -> int:
        return self.sum

    def toString(self) -> str:
        bits = bin(self.num)[2:]
        return "0" * (self.size - len(bits)) + bits

    def _get_xor_mask(self, index: int) -> int:
        return 1 << (self.size - index - 1)

    def _get_full_bitset(self) -> int:
        return 2 ** self.size - 1


class Solution:
    def __init__(self):
        self.commands_output = list()

    def run_commands(self, commands, arguments):
        bitset = None
        for index in range(len(commands)):
            if commands[index] == "Bitset":
                bitset = Bitset(arguments[index][0])
                self.commands_output.append(None)
                continue
            if commands[index] == "unfix":
                self.commands_output.append(bitset.unfix(arguments[index][0]))
                continue
            if commands[index] == "fix":
                self.commands_output.append(bitset.fix(arguments[index][0]))
                continue
            if commands[index] == "flip":
                self.commands_output.append(bitset.flip())
                continue
            if commands[index] == "all":
                self.commands_output.append(bitset.all())
                continue
            if commands[index] == "one":
                self.commands_output.append(bitset.one())
                continue
            if commands[index] == "count":
                self.commands_output.append(bitset.count())
                continue
            if commands[index] == "toString":
                self.commands_output.append(bitset.toString())
                continue

    def show_output(self):
        return self.commands_output
