class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and c == '*':
                stack.pop()
            else:
                stack.append(c)
        stack = [el for el in stack if el != '*']         
        return "".join(stack)
    
s_str = "leet**cod*e"
s_str = "erase*****"
s_str = "*"
sol_obj = Solution()
result = sol_obj.removeStars(s_str)
print("result: ", result)

