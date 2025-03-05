# Given a list of unique integers nums, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.


from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        
        for num in nums:
            res += [subset + [num] for subset in res]
        
        return res