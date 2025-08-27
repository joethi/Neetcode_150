from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l != r :
            if numbers[l] + numbers[r] == target :                
                return [l+1,r+1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:     
                r -= 1
        # return [l,r]

nums_lst = [1,2,3,4]
target = 3
sol_obj = Solution()
result = sol_obj.twoSum(nums_lst, target)
print("result", result)


