class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candiate1 = None
        candiate2 = None
        count1 = 0
        count2 = 0

        # Potential candiate
        for num in nums:
            if candiate1 == num:
                count1 += 1
            elif candiate2 == num:
                count2 += 1   
            elif count1 == 0:
                candiate1 = num
                count1 = 1
            elif count2 == 0:  
                candiate2 = num
                count2 = 1 
            else :
                count1 -= 1
                count2 -= 1    

        # Verfication of candiate
        count1 = count2 = 0
        for num in nums:
            if num == candiate1:
                count1 += 1
            elif num == candiate2 :
                count2 += 1
        
        result = []
        n = len(nums)

        if count1 > n//3:
            result.append(candiate1)
        if count2 > n//3:
            result.append(candiate2)

        return result    
               