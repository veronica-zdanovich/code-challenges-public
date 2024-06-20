from queue import PriorityQueue
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        trapped_water = 0
        elevations_queue = PriorityQueue()
        visited = set()

        m, n = len(heightMap), len(heightMap[0])

        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    elevations_queue.put((heightMap[i][j], i, j))
                    visited.add((i, j))

        neighbours_coords = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while not elevations_queue.empty():
            current_height, i, j = elevations_queue.get()
            for neighbour_i, neighbour_j in neighbours_coords:
                neighbour_i += i
                neighbour_j += j
                if 0 <= neighbour_i < m and 0 <= neighbour_j < n and (neighbour_i, neighbour_j) not in visited:
                    trapped_water += max(0, current_height - heightMap[neighbour_i][neighbour_j])
                    visited.add((neighbour_i, neighbour_j))
                    elevations_queue.put((max(current_height, heightMap[neighbour_i][neighbour_j]), neighbour_i, neighbour_j))

        return trapped_water
