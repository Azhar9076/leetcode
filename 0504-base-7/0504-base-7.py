class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        sign = ''
        if num < 0:
            sign = '-'
            num = abs(num)
        result = ''
        while num > 0:
            rem = num  % 7
            result += str(rem)
            num = num // 7
        return sign  + result[::-1]
