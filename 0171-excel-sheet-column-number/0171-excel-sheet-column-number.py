class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # IN : AB -> 28
        result = 0
        for ch in columnTitle :
            result = result * 26 + (ord(ch) - ord('A') + 1) #0 * 26  + 1 = 1 -> 'A'
        return result    