class Solution:
    def countPrimes(self, n: int) -> int:
        sieve = [True] * n

        for i in range(2, int(n ** 0.5) + 1):
            if sieve[i]:
                sieve[i * i:n:i] = [False] * len(sieve[i * i:n:i])

        return sum(sieve[2:])