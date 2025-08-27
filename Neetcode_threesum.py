from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # print("nums:", nums)
        nums.sort()
        # print("sorted nums: ", nums)
        tsum_lst = []
        # print("nums:", nums)
        for i in range(len(nums)-2):
            if nums[i] > 0 :
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = - nums[i]
            # print(f"i: {i}, target: {target}")
            l, r = i + 1, len(nums) - 1 
            while l < r :
                # print(f"i: {i}, l: {l}, r: {r}")
                # print(f"nums[i]: {nums[i]}, nums[l]: {nums[l]}, nums[r]: {nums[r]}")
                if (nums[l] + nums[r]) == target and l < r :                
                    tsum_lst.append([-target, nums[l],nums[r]])
                    # print("tsum_lst: ", tsum_lst)
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    print(f"l: {l}, r: {r}")    
                elif (nums[l] + nums[r]) < target :
                    l += 1
                elif (nums[l] + nums[r]) > target :     
                    r -= 1

        return tsum_lst
    
nums_lst = [-1,0,1,2,-1,-4]
# nums_lst = [3, 1, 4, 1, 5, 9]
# print("nums_lst.sort(): ", nums_lst.sort())
sol_obj = Solution()
result = sol_obj.threeSum(nums_lst)
print("result", result)

