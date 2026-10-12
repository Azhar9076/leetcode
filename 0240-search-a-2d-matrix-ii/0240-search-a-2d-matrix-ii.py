class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j = len(matrix[0]) - 1
        row , col  = len(matrix), len(matrix[0]) 

        while i < row and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else :
                i += 1
        return False               


