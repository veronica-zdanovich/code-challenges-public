class DSU:
    def __init__(self, max_size: int):
        self._max_size = max_size
        self._actual_opened = 0
        self._roots = [i for i in range(max_size)]
        self.ranks = [0 for _ in range(max_size)]

    def insert(self, id: int):
        """ Insert a new unconnected element with the given id """
        if self.contains(id):
            return

        self.ranks[id] += 1
        self._actual_opened += 1

    def contains(self, id: int) -> bool:
        """ Check if the given id is present in the DSU """
        return self.ranks[id] != 0

    def join(self, p: int, q: int):
        """ Join the two clusters containing p and q """
        p_root = self.find_root(p)
        q_root = self.find_root(q)
        if p_root == q_root:
            return

        if self.ranks[p_root] < self.ranks[q_root]:
            self._roots[p_root] = q_root
            self.ranks[q_root] += self.ranks[p_root]
        else:
            self._roots[q_root] = p_root
            self.ranks[p_root] += self.ranks[q_root]

    def find_root(self, i: int) -> int:
        while i != self._roots[i]:
            self._roots[i] = self._roots[self._roots[i]]
            i = self._roots[i]
        return i

    def connected(self, p: int, q: int) -> bool:
        """ Check if p and q are in the same cluster """
        p_root = self.find_root(p)
        q_root = self.find_root(q)
        return p_root == q_root

    def size(self) -> int:
        """ Return the actual number of elements in the DSU """
        return self._actual_opened

    def capacity(self) -> int:
        """ Return the maximum number of elements in the DSU """
        return self._max_size
