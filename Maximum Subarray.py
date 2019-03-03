class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # DP - recurrence relation : opt[i] = max(nums[i],nums[i]+opt[i-1])
        size = len(nums)
        result = [None] * size
        result[0] = nums[0]
        for i in range(1, size):
            result[i] = max(nums[i], result[i-1] + nums[i])
        
        return max(result)
