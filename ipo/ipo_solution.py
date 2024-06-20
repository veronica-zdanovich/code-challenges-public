from queue import PriorityQueue
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = PriorityQueue()
        for i in range(len(profits)):
            projects.put((capital[i], profits[i]))
        max_profits = PriorityQueue()
        for i in range(k):
            while not projects.empty() and projects.queue[0][0] <= w:
                capital, profit = projects.get()
                max_profits.put(-profit)
            if not max_profits.empty():
                profit = -max_profits.get()
                w += profit

        return w

