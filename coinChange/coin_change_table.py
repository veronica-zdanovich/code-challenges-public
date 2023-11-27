from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        max_value = 2**32 - 1
        table = [max_value if i != 0 else 0 for i in range(amount + 1)]

        for prev_amount, item in enumerate(table):
            for coin in coins:
                new_amount = prev_amount + coin
                if new_amount <= amount:
                    table[new_amount] = min(table[new_amount], table[prev_amount] + 1)

        if table[amount] == max_value:
            return -1
        return table[amount]
