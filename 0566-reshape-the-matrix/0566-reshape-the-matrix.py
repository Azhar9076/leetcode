import numpy as np

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        mat = np.array(mat)
        
        if mat.size == r * c:
            result = mat.reshape(r,c)
        else :
            result = mat
        return result.tolist()