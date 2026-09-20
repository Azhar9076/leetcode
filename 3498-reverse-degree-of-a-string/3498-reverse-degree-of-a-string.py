class Solution:
    def reverseDegree(self, s: str) -> int:
        reverse_value = 0
        value = 0
        for i in range (len(s)):
            reverse_value = 26 - (ord(s[i]) - ord('a'))
            value += (i + 1) * reverse_value
        return value    