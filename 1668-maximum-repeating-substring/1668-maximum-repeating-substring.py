class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        dp = word
        count = 0
        while dp in sequence:
            count += 1
            dp += word
        return count        