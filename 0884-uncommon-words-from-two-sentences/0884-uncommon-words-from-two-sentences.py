class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        s = s1.split() + s2.split()
        hash = {}

        for word in s:
            hash[word] = hash.get(word, 0) + 1

        result = []
        for ans in hash:
            if  hash[ans] == 1:
                result.append(ans)
        return result        