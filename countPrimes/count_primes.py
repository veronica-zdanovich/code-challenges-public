from math import sqrt, floor


class Solution:
    def countPrimes(self, n):
        if n < 3:
            return 0

        primes_list = [True for _ in range(n + 1)]  # 0 .. n + 1
        primes_list[0] = primes_list[1] = False  # 0, 1 - False
        primes_list[n] = False  # counter should be definitely less then n

        for prime_index in range(2, floor(sqrt(n)) + 1):
            prime = primes_list[prime_index]
            if prime == 0:
                continue

            for next_num in range(prime_index * prime_index, n + 1, prime_index):
                primes_list[next_num] = False

        return sum(primes_list)
