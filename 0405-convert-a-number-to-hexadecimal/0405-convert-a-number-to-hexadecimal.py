class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        num &= 0xffffffff  
        
        hex_char = "0123456789abcdef"
        ans = ""
        
        while num:
            digit = num & 15  
            ans = hex_char[digit] + ans
            num >>= 4
        
        return ans
