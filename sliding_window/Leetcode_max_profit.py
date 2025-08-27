from typing import List
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         l, r = 0, 1
#         max_price = max(0,prices[r]-prices[l])
#         while l < r and r < len(prices)-1:
#             print(f"l:{l},r:{r}")
#             if prices[r] < prices[l]:
#                 l = r
#             r += 1                
#             max_price = max(max_price,prices[r]-prices[l])

#         return max_price
# prices = [7,1,5,3,6,4]
# sol_obj = Solution()
# print(sol_obj.maxProfit(prices))   

def optimizeServerLoad(serverCapacity, serverLoad):
    # Sort serverCapacity in descending order
    sorted_capacity = sorted(serverCapacity, reverse=True)
    # Sort serverLoad in ascending order
    sorted_load = sorted(serverLoad)
    
    # Combine sorted_capacity and sorted_load
    # and assign the loads in the order
    result = [0] * len(serverLoad)
    for i, capacity in enumerate(sorted_capacity):
        result[serverCapacity.index(capacity)] = sorted_load[i]
    
    return result

# Example usage
serverCapacity = [4, 5, 6]
serverLoad = [1, 2, 3]
print(optimizeServerLoad(serverCapacity, serverLoad))

