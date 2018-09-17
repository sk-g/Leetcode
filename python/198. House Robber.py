class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) < 3:
            return max(nums)
        # first = nums[0]
        # second = max(nums[0],nums[1])
        # s = 0
        # for i in range(2,len(nums)):
        #     s = max(first+nums[i],second)
        #     first = second
        #     second = s
        # return s
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[-1]
                