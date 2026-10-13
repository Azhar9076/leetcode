class Solution:
    def findComplement(self, num: int) -> int:
        num = bin(num) [2:]
        complement = ''
        for n in num:
            if n == '0':
                complement += str(1)
            else :
                complement += str(0)
        return  int(complement, 2)