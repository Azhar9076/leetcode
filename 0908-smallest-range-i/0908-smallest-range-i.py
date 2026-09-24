class Solution:
    def smallestRangeI(self, nums: list[int], k: int) -> int:
        maxium = max(nums)
        minimum = min(nums)
        return max(0, maxium - minimum - 2 * k)