from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        ct_ct = [0] * (n + 1)
        for c in citations:
            if c > n:
                ct_ct[n] += 1
            else:
                ct_ct[c] += 1
        h = n        
        papers = ct_ct[n]
        while papers < h:
            h -= 1
            papers += ct_ct[h]

        return h
        # return h
citations = [1,3,1]
sol_obj = Solution()
print(sol_obj.hIndex(citations))


