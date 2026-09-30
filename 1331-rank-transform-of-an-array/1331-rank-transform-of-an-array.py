class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        array = sorted(arr)
        result = {}
        r = 1
        for i, ar in enumerate(array):
            if ar not in result:
                result[ar] = r
                r += 1
        return [result[x] for x in arr]        