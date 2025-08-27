from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num,0)
        srt_lst = list(count.keys())
        n = len(srt_lst)
        for i in range(n):
            for j in range(n-i-1):
                if count[srt_lst[j]] < count[srt_lst[j+1]]:
                    srt_lst[j], srt_lst[j+1] = srt_lst[j+1], srt_lst[j]
                    print("srt_lst: ", srt_lst)

        return srt_lst[:k]

nums_lst = [1,2,2,2,3,3,4,4,4]
sol_obj = Solution()
result = sol_obj.topKFrequent(nums_lst, 2)
print("result", result)

