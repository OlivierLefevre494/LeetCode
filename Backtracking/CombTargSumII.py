#You are given an array of integers candidates, which may contain duplicates, and a target integer target. 
# Your task is to return a list of all unique combinations of candidates where the chosen numbers sum to target.
#Each element from candidates may be chosen at most once within a combination. The solution set must not contain duplicate combinations.
#You may return the combinations in any order and the order of the numbers in each combination can be in any order.
from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # sort list
        candidates.sort()
        #DFS, BUT EACH NUM CAN BE PICKED ONLY ONCE
        i = 0
        def dfs(i, cur, total):
            if total==target:
                if cur.copy() not in res:
                    res.append(cur.copy())
                return
            if i>=len(candidates) or total>target:
                return
            #DFS NEXT ITER, EITHER DONT ADD NUM
            dfs(i+1, cur, total)
            cur.append(candidates[i])
            # OR ADD NUM
            dfs(i+1, cur, total + candidates[i])
            cur.pop()
        dfs(0, [], 0)
        return res