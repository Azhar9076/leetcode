class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        hashcount = {}
        for n in nums:
            hashcount[n] = hashcount.get(n, 0) + 1
        target = len(nums) // 2
        for key, value in hashcount.items():
            if value == target:
                return key