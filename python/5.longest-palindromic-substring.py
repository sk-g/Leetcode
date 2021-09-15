#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
from typing import *
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(s, left, right):
            while left >= 0 and right < len(s) and s[left] ==  s[right]:
                left -= 1
                right += 1
            return s[left + 1: right]
        n = len(s)
        if n < 2:
            if s == s[::-1]:    return s
            return ""
        res = ""
        for i in range(n - 1):
            res = max(res, expand(s, i, i), expand(s, i, i + 1), key=len)
        return res
# @lc code=end

