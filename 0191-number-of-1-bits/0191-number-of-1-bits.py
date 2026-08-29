class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)[2:]
        count = 0
        for i in binary:
            if i != '0':
                count += 1
        return count        