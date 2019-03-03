#You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

#Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

class Solution:
    def rob(self, nums: List[int]) -> int:
        # DP : Recurrence relation : opt[i] = max(opt[i-1], opt[i-2]            + nums[i]) 
        size = len(nums)
        opt = [None] * (size)
        if(size == 0):
            opt = [None] * 1
            opt[0] = 0
        elif(size == 1):
            opt = [None] * 2
            opt[0] = nums[0]
        else :  
            opt[0] = nums[0]
            opt[1] = max(nums[0], nums[1])
        for i in range(2,size):
            opt[i] = max(opt[i-1], opt[i-2] + nums[i])
        
        return opt[size-1]
