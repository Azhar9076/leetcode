import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        words = re.sub(r'[^a-zA-Z\s]', ' ', paragraph).lower().split()
        banned = set(banned)

        freq = {}

        for word in words:
            if word not in banned:
                freq[word] = freq.get(word, 0) + 1

        return max(freq, key=freq.get)