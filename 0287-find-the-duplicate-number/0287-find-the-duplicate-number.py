class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # nums.sort()
        # n = len(nums)

        # for i in range (1, n):
        #     if nums[i] == nums[i+1]:
        #         return nums[i]
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            count = 0

            for num in nums:
                if num <= mid:
                    count += 1

            if count <= mid:
                low = mid + 1
            else:
                high = mid

        return low            