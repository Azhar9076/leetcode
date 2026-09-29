class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        num = sorted(nums)
        result = {}
        for i, n in enumerate(num):
            if n not in result:
                result[n] = i
        return [result[x] for x in nums]        
