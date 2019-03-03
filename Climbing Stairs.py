# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct # ways can you climb to the top?

# Note: Given n will be a positive integer.
class Solution:
    def climbStairs(self, n: int) -> int:
        # DP : Recurrence Relation :  opt[i] = opt[i-1] + opt[i-2]
        opt = [None] * (n + 2)
        
        opt[0] = 1
        opt[1] = 2
        
        for i in range(2, n):
            opt[i] = opt[i-1] + opt[i-2]
        return opt[n-1]
