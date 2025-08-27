from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l, r = 0, 0
        while r < (len(nums) - 1):
            max_ind = l
            for i in range(l,r+1):
               max_ind = max(max_ind,i + nums[i])
            l = r + 1
            r = max_ind
            res += 1
        return res


nums = [2,3,1,1,4]
sol_obj = Solution()
print(sol_obj.jump(nums))


