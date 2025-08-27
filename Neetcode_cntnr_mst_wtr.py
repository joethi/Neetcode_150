from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        res  = 0
        while l < r :
            area = (r-l)* min(heights[l],heights[r])
            res = max(area, res)
            if heights[r] < heights[l] :
                r -= 1         
            else:
                l += 1      
        return res

height = [1,7,2,5,4,7,3,6]
sol_obj = Solution()
result = sol_obj.maxArea(height)
print("result", result)