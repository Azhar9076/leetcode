class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        count = {}
        for i in range (lowLimit, highLimit +1):
            total = 0
            while i > 0:
                digit = i % 10
                total += digit
                i //= 10
            count[total] = count.get(total, 0) + 1
        return max(count.values())    