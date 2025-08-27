from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # Sort candidates to handle duplicates
        res = []  # Initialize result list

        def backtrack(cur, pos, target):
            if target == 0:  # Base case: target is met
                res.append(cur.copy())  # Add current combination to result
                return
            if target < 0:  # Base case: target exceeded
                return
            
            prev = -1  # Variable to track the previous candidate
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:  # Skip duplicates
                    continue
                cur.append(candidates[i])  # Add current candidate
                backtrack(cur, i + 1, target - candidates[i])  # Recursive call
                cur.pop()  # Backtrack by removing last candidate
                prev = candidates[i]  # Update previous candidate

        backtrack([], 0, target)  # Initial call to the backtrack function
        return res  # Return the final result
    
candidates_lst = [2,3,6,7]
target_val = 7 
sol_obj = Solution()
sol_obj.combinationSum2(candidates_lst,target_val)

