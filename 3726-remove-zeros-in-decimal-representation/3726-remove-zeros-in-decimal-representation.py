class Solution:
    def removeZeros(self, n: int) -> int:
        decimal = 0
        place = 1
        result = 0
        while n > 0:
            decimal = n % 10
            if decimal != 0:
                result += decimal * place
                place *= 10
            n //= 10     

        return result    
