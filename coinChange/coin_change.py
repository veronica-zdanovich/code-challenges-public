from typing import List


class Solution:
    def __init__(self):
        self.cache = dict()

    def change_coin(self, coins: List[int], amount: int, coins_edge_index) -> int:
        if amount == 0:
            return 0

        if amount < 0:
            return -1

        if coins_edge_index < 0:
            return -1

        cached_amount = self.cache.get(amount * 100 + len(coins))
        match cached_amount:
            case None:
                pass
            case amount:
                return amount

        with_coin = self.change_coin(coins[:coins_edge_index + 1], amount - coins[coins_edge_index], coins_edge_index)
        without_coin = self.change_coin(coins[:coins_edge_index], amount, coins_edge_index - 1)

        if with_coin >= 0 and without_coin >= 0:
            result = min(with_coin + 1, without_coin)
        elif with_coin >= 0:
            result = with_coin + 1
        else:
            result = without_coin

        self.cache[amount * 100 + len(coins)] = result
        return result

    def coinChange(self, coins: List[int], amount: int) -> int:
        coins_edge_index = len(coins) - 1
        return self.change_coin(coins, amount, coins_edge_index)
