class Solution:
    def isBalanced(self, num: str) -> bool:
        even = 0
        odd = 0
        for i in range (len(num)):
            digit = int(num[i])  
            if i % 2 == 0:
                even += digit
            else:
                odd += digit
        return even == odd
           

