from collections import defaultdict
from typing import List
'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.
'''


class Solution:
    def mark_neighbours_as_visited(self, i: int, j: int, grid: List[List[str]], island_id: int, visited_nodes: dict):
        if visited_nodes.get((i, j)):
            return

        visited_nodes[(i, j)] = island_id

        if i < len(grid) - 1 and grid[i + 1][j] == "1":
            self.mark_neighbours_as_visited(i + 1, j, grid, island_id, visited_nodes)  # O(MxN)

        if j < len(grid[i]) - 1 and grid[i][j + 1] == "1":
            self.mark_neighbours_as_visited(i, j + 1, grid, island_id, visited_nodes)

        if i > 0 and grid[i - 1][j] == "1":
            self.mark_neighbours_as_visited(i - 1, j, grid, island_id, visited_nodes)

        if j > 0 and grid[i][j - 1] == "1":
            self.mark_neighbours_as_visited(i, j - 1, grid, island_id, visited_nodes)
        return

    def num_islands(self, grid: List[List[str]]) -> int:
        visited_nodes = defaultdict(int)
        island_id = 0
        island_ids = []

        for i, row in enumerate(grid):  # O(M)
            for j, column in enumerate(grid[i]):  #O(N)
                if visited_nodes.get((i, j)):  #O(1)
                    continue

                if grid[i][j] == "0":
                    continue

                self.mark_neighbours_as_visited(i, j, grid, island_id + 1, visited_nodes)
                island_id += 1
                if visited_nodes:
                    island_ids.append(island_id)
        if len(island_ids) == 0:
            return island_id
        return max(island_ids)
