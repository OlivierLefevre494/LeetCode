#You are given an integer array nums where nums[i] represents the amount of money the ith house has. 
# The houses are arranged in a straight line, i.e. the ith house is the neighbor of the (i-1)th and (i+1)th house.
#You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.
#Return the maximum amount of money you can rob without alerting the police.
#
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        if len(nums)==1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        
        return dp[-1]