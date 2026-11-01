class Solution:
    def reverseBits(self, n: int) -> int:
        n = bin(n) [2:]
        n = n.zfill(32)
        reverse_bin = n[::-1]
        return int(reverse_bin, 2)