from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        fluctuations = list()
        stack = list()
        mapping = dict()

        for i in range(len(temperatures)):
            while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]:
                top = stack.pop()
                mapping[top] = i - top
            stack.append(i)

        while len(stack) > 0:
            mapping[stack.pop()] = 0

        for i in range(len(temperatures)):
            fluctuations.append(mapping[i])

        return fluctuations