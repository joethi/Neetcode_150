#TODO: CORRECT THE SOLUTION.
# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         dict_map = {"[":"]", "{":"}", "(":")"}
#         l, r = 0, 1
#         if len(s)%2 != 0:
#             return False            
#         for i in range(len(s)-1):
#             print("i: ", i)
#             stack.append(s[i])
#             print("appended stack: ", stack)
#             print("s[i+1]: ", s[i+1])
#             if s[i+1] == dict_map[stack[i]]:
#                 stack.pop()
#                 print("popped stack: ", stack)                        
#         return not stack 

# s_str = "([{}])"
# sol_obj = Solution()
# result = sol_obj.isValid(s_str)
# print("result: ", result)
