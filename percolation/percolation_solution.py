import random
import time
from typing import List

from dsu.dsu import DSU


class Percolation:
    def __init__(self, size):
        self.grid_size = size
        self.dsu = DSU(size**2)

    def _open(self, id: int):
        self.dsu.insert(id)
        neighbours = self._find_neighbours(id)
        for neighbour in neighbours:
            self.dsu.join(id, neighbour)

    def _find_neighbours(self, id: int) -> List[int]:
        neighbour_ids = list()
        if id - 1 >= 0 and self.dsu.ranks[id - 1] > 0:
            neighbour_ids.append(id - 1)
        if id - self.grid_size >= 0 and self.dsu.ranks[id - self.grid_size] > 0:
            neighbour_ids.append(id - self.grid_size)
        if id + 1 < self.grid_size**2 and self.dsu.ranks[id + 1] > 0:
            neighbour_ids.append(id + 1)
        if id + self.grid_size < self.grid_size**2 and self.dsu.ranks[id + self.grid_size] > 0:
            neighbour_ids.append(id + self.grid_size)
        return neighbour_ids

    def _percolates(self) -> bool:
        upper_edge_roots = [self.dsu.find_root(i) for i in range(0, self.grid_size)]
        lower_edge_roots = [self.dsu.find_root(i) for i in
                            range(self.grid_size ** 2 - self.grid_size, self.grid_size ** 2)]
        return bool(set(upper_edge_roots) & set(lower_edge_roots))

    def calculate(self) -> int:
        while not self._percolates():
            id = random.randint(0, self.grid_size**2 - 1)
            self._open(id)
        return self.dsu.size()


if __name__ == "__main__":
    n = 20

    times = 1000
    number_of_open_sites = list()
    start_time = time.time()
    for i in range(times):
        percolation = Percolation(n)
        open_sites = percolation.calculate()
        number_of_open_sites.append(open_sites)
    end_time = time.time() - start_time
    percentage = lambda sites: sites / (n * n)
    mean = sum([percentage(open_sites) for open_sites in number_of_open_sites]) / times

    print(f"mean {mean}")
    print(f"time {end_time}")
