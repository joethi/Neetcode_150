from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_zero = False
        n_rows, n_cols = len(matrix), len(matrix[0])
        for r in range(1,n_rows):
            for c in range(n_cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0 
                    matrix[r][0] = 0
        for c in range(n_cols):
            if matrix[0][c] == 0:
                row_zero = True
        for r in range(1,n_rows):
            if matrix[r][0] == 0:
                matrix[r][:] = [0] * n_cols
        for c in range(n_cols):        
            if matrix[0][c] == 0:
                for r in range(n_rows):
                    matrix[r][c] = 0
        if row_zero == True:
            matrix[0][:] = [0] * n_cols
        print(matrix)
        # return 
# matrix = [
#   [1,2,3],
#   [4,0,5],
#   [6,7,8]
# ]
matrix=[[-4,-2147483648,6,-7,0],[-8,6,-8,-6,0],[2147483647,2,-9,-6,-10]]
sol_obj = Solution()
print(sol_obj.setZeroes(matrix))