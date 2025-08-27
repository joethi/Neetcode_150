from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ind_vals = []
        non_ind_vals = []
        k = 0
        for i in range(len(nums)):
            if nums[i] == val:
               ind_vals.append(i)
               k += 1   
            else:
               non_ind_vals.append(i)
        for i in range(len(non_ind_vals)):
            nums[i] = nums[non_ind_vals[i]]
        print(nums)
        return k    
    
nums = [0,1,2,2,3,0,4,2]
sol_obj = Solution()
val = 2
print(sol_obj.removeElement(nums,val))



