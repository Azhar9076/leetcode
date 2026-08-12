class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        distinct = list(set(nums))
        if len(distinct) < 3:
            return max(distinct)
        distinct.remove(max(distinct))
        distinct.remove(max(distinct))
        return max(distinct)    