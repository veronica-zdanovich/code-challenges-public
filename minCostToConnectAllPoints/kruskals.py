from typing import List


class UnionFind:
    def __init__(self, length: int):
        self.roots = [i for i in range(length)]
        self.ranks = [0 for _ in range(length)]

    def union(self, i_root: int, j_root: int, rank: int):
        if self.ranks[i_root] > self.ranks[j_root]:
            self.roots[j_root] = i_root
            self.ranks[i_root] += self.ranks[j_root] + rank
        else:
            self.roots[i_root] = j_root
            self.ranks[j_root] += self.ranks[i_root] + rank

    def find_root(self, i: int) -> int:
        while i != self.roots[i]:
            self.roots[i] = self.roots[self.roots[i]]
            i = self.roots[i]
        return i


class Solution:
    def _manhattan_distance(self, start: List[int], end: List[int]) -> int:
        return abs(end[0] - start[0]) + abs(end[1] - start[1])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        weighted_edges = list()

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                distance = self._manhattan_distance(points[i], points[j])
                weighted_edges.append([distance, i, j])

        min_distance = 0
        added_edges = 0
        weighted_edges.sort(key=lambda x: x[0])

        uf = UnionFind(len(points))

        for distance, i, j in weighted_edges:
            i_root = uf.find_root(i)
            j_root = uf.find_root(j)
            if i_root == j_root:
                continue

            uf.union(i_root, j_root, distance)
            added_edges += 1

            min_distance += distance
            if added_edges == len(points) - 1:
                break

        return min_distance
