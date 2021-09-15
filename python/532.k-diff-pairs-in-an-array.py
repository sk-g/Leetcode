#
# @lc app=leetcode id=532 lang=python3
#
# [532] K-diff Pairs in an Array
#

# @lc code=start
from typing import *
from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        counts = Counter(nums)
        res = 0
        """
        a - b = k
        a = b + k
        """
        for num in counts:
            if k > 0 and num + k in counts:
                res += 1
            elif k == 0 and counts[num] > 1:
                res += 1
        return res
# @lc code=end

