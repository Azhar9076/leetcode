class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maximum = max(nums)
        count = 0

        for num in nums:

            count += maximum - num

        return count    