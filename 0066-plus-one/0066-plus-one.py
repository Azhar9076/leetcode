class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
    #     i = len(digits) - 1 #3-1 = 2
    #     while i > 0: # N > 0
    #         if digits:
    #             digits[i] = digits[i] + 1 # i + 1 = i
    #             break
    #     return digits        
        i = len(digits) - 1 #3-1 = 2
        while i >= 0: # N > 0
            if digits[i] < 9:
                digits[i] = digits[i] + 1 # i + 1 = i
                return digits
            digits[i] = 0
            i-=1    
        return [1] + digits