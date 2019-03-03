# On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
# Once you pay the cost, you can either climb one or two steps. 
# You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, 
# or the step with index 1.

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # DP - Recurrence Relation : opt[i] = min(opt[i-1] + cost[i-1], opt[i-2]           + cost[i-2])
        size = len(cost)
        opt = [None] * (size + 1)
        opt[0] = 0
        opt[1] = 0
        
        for i in range(2, size + 1):
            print(i)
            opt[i] = min(opt[i-1] + cost[i-1], opt[i-2] + cost[i-2])
        return opt[size]
