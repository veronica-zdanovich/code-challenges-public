from collections import deque
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        visited = set()

        mutations = ["A", "T", "G", "C"]
        queue = deque()
        queue.append((startGene, 0))

        while len(queue) > 0:
            current_gene, counter = queue.popleft()

            if current_gene == endGene:
                return counter

            difference = 0

            for i in range(8):
                for alternation in mutations:
                    alter_gene = current_gene[0:i] + alternation + current_gene[i + 1:]
                    if alter_gene in bank and alter_gene not in visited:
                        queue.append((alter_gene, counter + 1))
                        visited.add(alter_gene)
                        difference += 1
                        break
                if difference >= 2:
                    break

        return -1
