from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_pft = 0
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                max_pft = max(max_pft,prices[r]-prices[l])    
            r += 1    

        return max_pft

price_list = [10, 1, 5, 6, 7, 1] #Ans: 6
# price_list = [10,8,7,5,2]  #Ans: 0
# price_list = [7,1,5,3,6,4] #Ans: 5

sol_obj = Solution()
result = sol_obj.maxProfit(price_list)
print("result: ", result)