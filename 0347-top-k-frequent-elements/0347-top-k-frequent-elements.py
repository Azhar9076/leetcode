class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hash = {}
        for key , value in enumerate (nums):
            hash[value] = hash.get(value ,0) + 1
        hash = sorted(hash.items(), key = lambda x:x[1], reverse = True)

        return [item[0] for item in hash[:k]]   