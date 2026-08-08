class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
    #    return nums + nums[::-1]
        revnums = []
        i = len(nums) - 1
        while i >= 0:
            revnums.append(nums[i])
            i -= 1
        return nums + revnums    
       