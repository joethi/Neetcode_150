from typing import List
# class Solution:
#     def encode(self, strs: List[str]) -> str:
#         str_mrgd = ""
#         for str in strs:
#             str_mrgd = str_mrgd + f"{len(str)}#" + str             
#         str_dcd_res = self.decode(str_mrgd)
#         return str_dcd_res
#     def decode(self, s: str) -> List[str]:         
#         str_dcd = []
#         print("s before elimination: ", s)
#         while s:
#             num_ct = int(s[0])
#             print("num_ct: ", num_ct)
#             str_dcd.append(s[2:num_ct+2])
#             print("str_dcd: ", str_dcd)
#             s = s[num_ct+2:]    
#             print("s after elimination: ", s) 
#         return str_dcd

class Solution:
    def encode(self, strs: List[str]) -> str:
        str_mrgd = ""
        for str in strs:
            str_mrgd = str_mrgd + f"{len(str)}#" + str             
        return str_mrgd
    def decode(self, s: str) -> List[str]:         
        str_dcd = []
        # print("s before elimination: ", s)
        while s:
            ct = 0
            num_str = ""
            while s[ct] != "#":
                num_str = num_str + s[ct]   
                ct += 1
            num_ct = int(num_str)
            # print("num_ct: ", num_ct)            
            str_dcd.append(s[ct+1:num_ct+ct+1])
            # print("str_dcd: ", str_dcd)
            s = s[num_ct+ct+1:]    
            # print("s after elimination: ", s) 
        return str_dcd

# str_list = ["neet", "code", "love", "you"]
# str_list = ["we","say",":","yes"]
str_list = ["we","say",":","yes","!@#$%^&*()"]
sol_obj = Solution()
s_str = sol_obj.encode(str_list)
print("s_str: ", s_str)
result = sol_obj.decode(s_str)
print("result:", result)


