class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        hash = {}
        for num in nums:
            hash[num] = hash.get(num, 0) + 1
        sum = 0
        for key, value in hash.items():
            if value == 1:
                sum += key
        return sum        
