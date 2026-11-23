class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        freq = {}
        for a in arr:
            freq[a] = freq.get(a, 0) + 1
        return len(freq.values()) == len(set(freq.values()))
            