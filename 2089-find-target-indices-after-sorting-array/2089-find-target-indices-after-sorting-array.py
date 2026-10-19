class Solution(object):
    def targetIndices(self, nums, target):
        
        nums.sort()
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return [i for i in range (len(nums)) if nums[i] == target]
            elif nums[mid] <= target:
                low = mid + 1
            else :
                high = mid - 1
        return []