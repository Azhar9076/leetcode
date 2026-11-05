class Solution:
    def specialArray(self, nums: list[int]) -> int:
        for x in range(len(nums) + 1):
            count = 0
            for num in nums:
                if num >= x:
                    count += 1
            
            if x == count :
                return x
        
        return -1