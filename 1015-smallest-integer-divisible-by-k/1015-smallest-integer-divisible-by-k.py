class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1        
        reminder = 0
        length  = 0
        while True:
            reminder = (reminder * 10 + 1) % k
            length += 1
            if reminder == 0:
                return length
        