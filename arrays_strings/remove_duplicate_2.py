from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        j = 1
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1] and j < 2:
                nums[k] = nums[i+1]
                j += 1
                k += 1
            elif nums[i] == nums[i+1] and j >= 2:
                j += 1
            else:
                nums[k] = nums[i+1]
                k += 1
                j = 1
        print(nums)
nums = [1,1,1,2,2,3]
sol_obj = Solution()
print(sol_obj.removeDuplicates(nums))