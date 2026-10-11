class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        result = 0
        n = len(mat)
        for i in range (n):
            result += mat[i][i]
            result += mat[i][n - i - 1]
        if n % 2 == 1:
            result -= mat[n//2][n//2] 
        return result        