from typing import List, Optional


class RangeModule:

    def __init__(self):
        self.intervals = list()

    def _subtract_intervals(self, interval1: List[int], interval2: List[int]) -> List:
        result = []
        a, b = interval1
        c, d = interval2

        if b <= c or d <= a:
            result.append([a, b])
        elif a < c and b <= d:
            result.append([a, c])
        elif a >= c and b > d:
            result.append([d, b])
        elif a < c and b > d:
            result.extend([[a, c], [d, b]])
        else:
            result = []

        return result

    def addRange(self, left: int, right: int) -> None:
        new_intervals = list()
        inserted = False

        for interval in self.intervals:
            if interval[1] < left:
                new_intervals.append(interval)
            elif right < interval[0]:
                if not inserted:
                    new_intervals.append([left, right])
                    inserted = True
                new_intervals.append(interval)
            else:
                left = min(left, interval[0])
                right = max(right, interval[1])

        if not inserted:
            new_intervals.append([left, right])
        self.intervals = new_intervals

    def queryRange(self, left: int, right: int) -> bool:
        low, high = 0, len(self.intervals) - 1
        while low <= high:
            mid = (low + high) // 2
            interval = self.intervals[mid]
            if interval[0] <= left <= interval[1] and interval[0] <= right <= interval[1]:
                return True
            if right > interval[1]:
                low = mid + 1
            else:
                high = mid - 1
        return False

    def removeRange(self, left: int, right: int) -> None:
        new_intervals = []
        for interval in self.intervals:
            new_intervals.extend(self._subtract_intervals(interval, [left, right]))
        self.intervals = new_intervals


class Solution:
    def run_commands(self, commands: List[str], arguments: List[Optional[List]]):
        range_module = None
        commands_output = list()
        for index in range(len(commands)):
            if commands[index] == "RangeModule":
                range_module = RangeModule()
                commands_output.append(None)
                continue
            if commands[index] == "addRange":
                commands_output.append(range_module.addRange(*arguments[index]))
                continue
            if commands[index] == "removeRange":
                commands_output.append(range_module.removeRange(*arguments[index]))
                continue
            if commands[index] == "queryRange":
                commands_output.append(range_module.queryRange(*arguments[index]))
                print(commands_output[-1])
                continue
        return commands_output
