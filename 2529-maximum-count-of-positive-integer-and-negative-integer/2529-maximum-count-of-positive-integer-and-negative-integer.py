class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        low , high = 0, len(nums)
        pos_count , neg_count = 0,0 
        while low < high:
            mid = (low + high) // 2
            if nums[mid] < 0:
                low = mid + 1
            else :
                high = mid
        neg_count = low
        low , high = 0, len(nums)
        while low < high:
            mid = (low + high) // 2
            if nums[mid] <= 0:
                low = mid + 1
            else :
                high = mid  
        pos_count = len(nums) - low              
        return max(pos_count, neg_count)        