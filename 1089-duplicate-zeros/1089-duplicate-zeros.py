class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        zeros = arr.count(0)
        
        i = n - 1
        j = n + zeros - 1  
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                arr.insert(i + 1, 0)   
                arr.pop()              
                i += 2                 
            else:
                i += 1
