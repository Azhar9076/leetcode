class Solution:
    def findComplement(self, num: int) -> int:
        nums = bin(num) [2:]
        complement = ''
        for n in nums:
            if n == '0':
                complement += str(1)
            else :
                complement += str(0)
        return  int(complement, 2)