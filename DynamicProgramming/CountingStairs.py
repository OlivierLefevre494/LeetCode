#You are given an integer n representing the number of steps to reach the top of a staircase. You can climb with either 1 or 2 steps at a time.
#Return the number of distinct ways to climb to the top of the staircase.

class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0
        num = n
        if num>2:
            count = count + self.climbStairs(num-2)
            count = count + self.climbStairs(num-1)
        else:
            if num==1:
                return count+1
            elif num==2:
                return count+2
        return count
