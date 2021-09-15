#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Medium (47.67%)
# Likes:    6568
# Dislikes: 303
# Total Accepted:    490.3K
# Total Submissions: 1M
# Testcase Example:  '[100,4,200,1,3,2]'
#
# Given an unsorted array of integers nums, return the length of the longest
# consecutive elements sequence.
# 
# You must write an algorithm that runs in O(n) time.
# 
# 
# Example 1:
# 
# 
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
# 
# 
# Example 2:
# 
# 
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# 
# 
# 
# Constraints:
# 
# 
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 
# 
#

# @lc code=start
from typing import *
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:    return 0
        nums = set(nums)
        res = 0
        running = 0
        low = min(nums)
        high = max(nums)
        current = 0
        for i in nums:
            if i - 1 not in nums:
                current = i
                running = 1
            while current + 1 in nums:
                current += 1
                running += 1
            res = max(res, running)
        return res
# @lc code=end

