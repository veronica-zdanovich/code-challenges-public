"""
write a function that, given a distance d and a stream
of floating point values received one at a time, checks for groups of
three values within d distance of one another. Store the floating point values
in memory as they are received. When a group of three values meeting the
distance criteria is found, return the three values and remove them from the
memory.
"""
from collections import defaultdict
from typing import Optional, List


class Conveyor:
    def __init__(self, distance: int):
        self.stream = list()
        self.distance = distance

    def add_value(self, new_item: int) -> Optional[List[int]]:
        self.stream.append(new_item)
        self.stream.sort()

        start = 0
        end = 2

        while start <= len(self.stream) - 3:
            if abs(self.stream[end] - self.stream[start]) <= self.distance:
                result = self.stream[start:end + 1]
                self.stream = self.stream[:start] + self.stream[end + 1:]
                return result

            start += 1
            end += 1

        return []
