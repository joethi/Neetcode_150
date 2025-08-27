from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        outputs = [1] * n
        for i in range(n):
            for j in range(n):
                if j != i:
                    outputs[i] = outputs[i] * nums[j]
        return outputs
            
num_lst = [1,2,4,6]
num_lst = [-1,0,1,2,3]
sol_obj = Solution()
result = sol_obj.productExceptSelf(num_lst)
print(result)