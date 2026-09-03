class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_even = float('inf')
        min_odd = float('inf')
        for i in nums1:
            if i%2==0:
                min_even = min(i,min_even)
            else :
                min_odd = min(i,min_odd)
        if  min_even == float('inf'):
            return True
        if min_odd == float('inf'):
            return True   
        return min_odd < min_even             