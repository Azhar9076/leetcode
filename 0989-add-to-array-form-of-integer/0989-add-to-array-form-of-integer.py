import sys
class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        sys.set_int_max_str_digits(0)
        result = 0
        arr = []
        for n in num:
            result = result * 10 + n
        total = result + k
        
        return [int(i) for i in str(total)]