class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        add = 0
        n = len(nums)
        for i in range(n):
            s = set()
            for j in range(i, n):
                s.add(nums[j])
                add += len(s) ** 2
        return add        
