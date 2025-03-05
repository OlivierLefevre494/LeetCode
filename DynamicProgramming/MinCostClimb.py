# You are given an array of integers cost where cost[i] is the cost of taking a step from the ith floor of a staircase. 
# After paying the cost, you can step to either the (i + 1)th floor or the (i + 2)th floor.
# You may choose to start at the index 0 or the index 1 floor.
# Return the minimum cost to reach the top of the staircase, i.e. just past the last index in cost.
from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if cost==[]:
            return 0
        if len(cost)==1:
            return min(cost[0], 0)
        else:
            return min(cost[-1]+self.minCostClimbingStairs(cost[:-1]), cost[-2]+self.minCostClimbingStairs(cost[:-2]))