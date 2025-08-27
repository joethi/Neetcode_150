class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # for c in s:
        #     dic_ct[f"{c}"] = dic_ct.get(f"{c}",0) + 1
        # ct_lst = []
        # for value in dic_ct.values(): 
        #     ct_lst.append(value)
        # if len(ct_lst) == 1:
        #     mx_str_len = max(ct_lst)    
        # else:    
        #     mx_str_len = max(ct_lst) + k
        dic_ct = {}
        mxct_rpt = 0
        max_len = 0
        l = 0 
        for r in range(len(s)):
            dic_ct[s[r]] = dic_ct.get(s[r],0) + 1
            mxct_rpt = max(mxct_rpt,dic_ct[s[r]])
            while (r - l + 1 - mxct_rpt) > k:
                dic_ct[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
            # print("l: ", l, "r: ", r)
        return max_len

strng = "AAABABB"
strng = "AAAA"
strng = "AABABBA"
k = 1
sol_obj = Solution()
result = sol_obj.characterReplacement(strng,k)
print("result", result)







