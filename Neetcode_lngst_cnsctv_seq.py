from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        print("nums_set: ", nums_set)
        longest = 0
        for num in nums_set:
            if (num-1) not in nums_set:
                length = 1
                while (num + length) in nums_set:
                    length += 1
                longest = max(length, longest)        

        return longest
    
nums_lst = [0,3,2,5,4,6,1,1]
sol_obj = Solution()
result = sol_obj.longestConsecutive(nums_lst)
print("result", result)

