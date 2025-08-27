class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        s_pld_lst = [s[0]] 
        for i in range(1,n-1):
            l = i - 1
            r = i + 1 
            s_pld = s[i]   
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    s_pld = s[l] + s_pld + s[r]
                    s_pld_lst.append(s_pld)
                    l -= 1
                    r += 1
                else: 
                    break
        for i in range(0,n-1):
            l = i
            r = i + 1
            s_pld = s[i]
            while r < n:  
                print("i: ", i)
                print("r: ", r)       
                if s[l] == s[r]:
                    s_pld = s_pld + s[r]
                    s_pld_lst.append(s_pld)
                    r += 1
                else:
                    break    
            print("s_pld_lst: ", s_pld_lst)        
        return max(s_pld_lst,key=len) 

s_str = "ababd"
s_str = "abbc"
s_str = "aaaa"
sol_obj = Solution()
result = sol_obj.longestPalindrome(s_str)
print(result)

