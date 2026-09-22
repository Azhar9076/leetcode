class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        left = 0
        while left < len(arr):
            right = 0
            while right < len(arr): 
                if right != left and arr[left] == arr[right] * 2:
                    return True
                right+= 1
            left += 1    
        return False    