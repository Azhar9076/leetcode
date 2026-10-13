class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        subsets = [[]]
        for num in nums:
            subsets += [subset + [num] for subset in subsets]
        return subsets    