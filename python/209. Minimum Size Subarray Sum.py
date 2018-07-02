#209. Minimum Size Subarray Sum
# same two pointer idea as mentioned in solution
# main idea is to precompute sums and then change 
# it on the go as per required.
class Solution:
    def minSubArrayLen(self, s, nums):
        n = len(nums)
        ans = float('inf')
        left = 0
        presum = 0
        for i in range(n):
            presum += nums[i]
            while (presum>=s):
                ans = min(ans,i-left+1)
                presum -= nums[left]
                left += 1
        if ans == float('inf'):
            return 0
        else:
            return ans
            