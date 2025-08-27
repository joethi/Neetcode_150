# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False 
#         for letter in s:
#             print("letter", letter)
#             if letter not in t:
#                 return False

#         return True

# s_str = "jar"
# t_str = "rab"
# sol_obj = Solution()
# result = sol_obj.isAnagram(s_str,t_str)
# print("result", result)
#
s = "jar"
t = "raj"
countS, countT = {}, {}
for i in range(len(s)):
    print("i: ", i)
    countS[s[i]] = 1 + countS.get(s[i], 0)
    print("countS: ", countS)
    countT[t[i]] = 1 + countT.get(t[i], 0)
    print("countT: ", countT)


