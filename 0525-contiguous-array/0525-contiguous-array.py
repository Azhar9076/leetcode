class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        max_len = 0

        first = {0:-1}
        for i in range (len(nums)):
            if nums[i] == 0:
                count -= 1
            else :
                count += 1
            if count in first:
                max_len = max(max_len, i-first[count])
            else:
                first[count] = i
        return max_len                  