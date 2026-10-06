class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        insertions = 0
        for ch in s:
            if ch == '(':
                count += 1
            else :
                if count > 0:
                    count -= 1
                else:
                    insertions += 1
        return count + insertions            