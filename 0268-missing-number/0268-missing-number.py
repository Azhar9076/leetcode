class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        
        nums_set = set(nums)

        for i in range(1, n + 1):
            if i not in nums_set:
                return i
        return None        

        
