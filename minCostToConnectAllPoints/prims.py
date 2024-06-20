from queue import PriorityQueue
from typing import List


class Solution:
    def _manhattan_distance(self, start: List[int], end: List[int]) -> int:
        return abs(end[0] - start[0]) + abs(end[1] - start[1])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = [[] for _ in range(len(points))]
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                distance = self._manhattan_distance(points[i], points[j])
                graph[i].append([distance, j])
                graph[j].append([distance, i])

        min_distance = 0

        visited = [False for _ in range(len(points))]
        min_heap = PriorityQueue()
        min_heap.put([0, 0])

        while not min_heap.empty():
            distance, start = min_heap.get()
            if not visited[start]:
                min_distance += distance
                visited[start] = True
                for weight, neighbour in graph[start]:
                    if not visited[neighbour]:
                        min_heap.put([weight, neighbour])

        return min_distance
