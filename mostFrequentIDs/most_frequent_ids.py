from collections import defaultdict
from queue import PriorityQueue
from typing import List


class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        answer = list()
        max_queue = PriorityQueue()
        max_queue.put([0, 0])
        num_occurrences = defaultdict(int)

        for i in range(len(nums)):
            num_occurrences[nums[i]] += freq[i]
            max_queue.put([-num_occurrences[nums[i]], nums[i]])

            while not max_queue.empty() and -max_queue.queue[0][0] != num_occurrences[max_queue.queue[0][1]]:
                max_queue.get()

            answer.append(-max_queue.queue[0][0])

        return answer
