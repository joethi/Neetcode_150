from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0 , len(nums) - 1
        min_lst = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                min_lst = min(min_lst, nums[l])
                break    
            m = (l + r) // 2
            min_lst = min(min_lst, nums[m])
            if nums[m] >= nums[l]:
                #search right
                l = m + 1
            else:
                #search left
                r = m - 1

        return min_lst


nums_lst = [3,4,5,6,1,2]
nums_lst = [4,5,0,1,2,3]
nums_lst = [4,5,6,7]
sol_obj = Solution()
result = sol_obj.findMin(nums_lst)
print("result", result)


