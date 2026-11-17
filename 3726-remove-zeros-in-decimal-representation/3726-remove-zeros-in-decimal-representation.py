class Solution:
    def removeZeros(self, n: int) -> int:
        decimal = str(n)
        ans = ''
        for i in range(len(decimal)):
            if decimal[i] != '0':
                ans += decimal[i]
        return int(ans)        
