from typing import List


class Solution:
    def has_horizontally_connected(self, row: int, col: int, n: int, grid: List[List[int]]):
        for horizontal_item in range(n):
            if horizontal_item == col:
                continue
            if grid[row][horizontal_item] == 1:
                return True
        return False

    def has_vertically_connected(self, row: int, col: int, m: int, grid: List[List[int]]):
        for vertical_item in range(m):
            if vertical_item == row:
                continue
            if grid[vertical_item][col] == 1:
                return True
        return False

    def find_connected_servers(self, row: int, col: int, m: int, n: int, grid: List[List[int]]):
        connected_servers = 0
        has_vertically_connected = self.has_vertically_connected(row, col, m, grid)
        has_horizontally_connected = self.has_horizontally_connected(row, col, n, grid)
        if has_vertically_connected or has_horizontally_connected:
            connected_servers += 1
        return connected_servers

    def countServers(self, grid: List[List[int]]) -> int:
        connected_servers = 0
        m = len(grid)
        n = len(grid[0])

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    continue
                connected_servers += self.find_connected_servers(row, col, m, n, grid)
        return connected_servers
