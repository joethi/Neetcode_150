from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit, maxprft_tmp = 0, 0
        while r < len(prices) and prices[l] > prices[r]:
            l += 1
            r += 1
        while r < len(prices):
            
            if r > 1 and prices[r] < prices[r-1]:
                maxProfit += maxprft_tmp
                
                l = r    
            maxprft_tmp = max(maxprft_tmp,prices[r]-prices[l])
            maxProfit += maxprft_tmp
            r += 1
        return maxProfit
    
prices = [1,2,3,4,5]
# prices = [7,6,4,3,1]
# prices = [7,1,5,3,6,4]
sol_obj = Solution()
print(sol_obj.maxProfit(prices))
