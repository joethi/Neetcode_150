from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        return dp[0][n-1]
    
string = "hotspot"
word_dict = ["hot","spot"]    
sol_obj = Solution()
print(sol_obj.wordBreak(string,word_dict))