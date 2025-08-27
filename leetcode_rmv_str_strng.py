class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for l in s:
           if stack and l == "*":
               stack.pop()
           else:
               stack.append(l)      
        return "".join(stack)
    
strng = "leet**cod*e"
strng = "erase*****"
rmvstr_obj = Solution()
print("remove star: ", rmvstr_obj.removeStars(strng))    