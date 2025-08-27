from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix[0])-1
        while l < r:
            top, bottom = l, r
            for i in range(r-l):
                temp = matrix[top][l+i]
                matrix[top][l+i] = matrix[bottom-i][l]
                matrix[bottom-i][l] = matrix[bottom][r-i]
                matrix[bottom][r-i] = matrix[top+i][r]
                matrix[top+i][r] = temp 
            r -= 1
            l += 1
            print(matrix)
        # return matrix


matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

sol_obj = Solution()
print(sol_obj.rotate(matrix))



