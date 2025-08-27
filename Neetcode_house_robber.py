from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        if n == 1:
            return dp[0]
        dp[1] = max(nums[0],nums[1])
        if n == 2:
            return dp[1]
        for i in range(2,n):
            dp[i] = max(dp[i-2]+nums[i],dp[i-1])    

        return dp[-1]         



nums = [2,9,8,3,6]
nums = [1,1,3,3]
sol_obj = Solution()
result = sol_obj.rob(nums)
print("result", result)

