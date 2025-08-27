class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        S_set = set()
        l, r =  0, 0
        max_len = 1 
        while l < (len(s)-1):    
            if s[r] not in S_set: 
                S_set.add(s[r])
                max_len = max(max_len, r - l + 1)
                r += 1
                print("r: ", r)
                if r > (len(s)-1):
                    break
            else:
                S_set.remove(s[l])
                l += 1           
            print("S_set: ", S_set)      
        return max_len
    
strng = "zxyzxyz"
strng = "xxxx"
sol_obj = Solution()
result = sol_obj.lengthOfLongestSubstring(strng)
print("result", result)





