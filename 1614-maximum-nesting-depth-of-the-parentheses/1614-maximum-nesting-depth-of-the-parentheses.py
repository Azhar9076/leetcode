class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        maxdepth = 0
        for char in s:
            if char == '(':
                count += 1
            if char == ')':
                count -= 1
            maxdepth = max(maxdepth, count)
        return maxdepth    