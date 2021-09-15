#
# @lc app=leetcode id=1520 lang=python3
#
# [1520] Maximum Number of Non-Overlapping Substrings
#
# https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/description/
#
# algorithms
# Hard (37.01%)
# Likes:    381
# Dislikes: 49
# Total Accepted:    9.3K
# Total Submissions: 25.2K
# Testcase Example:  '"adefaddaccc"'
#
# Given a string s of lowercase letters, you need to find the maximum number of
# non-empty substrings of s that meet the following conditions:
# 
# 
# The substrings do not overlap, that is for any two substrings s[i..j] and
# s[k..l], either j < k or i > l is true.
# A substring that contains a certain character c must also contain all
# occurrences of c.
# 
# 
# Find the maximum number of substrings that meet the above conditions. If
# there are multiple solutions with the same number of substrings, return the
# one with minimum total length. It can be shown that there exists a unique
# solution of minimum total length.
# 
# Notice that you can return the substrings in any order.
# 
# 
# Example 1:
# 
# 
# Input: s = "adefaddaccc"
# Output: ["e","f","ccc"]
# Explanation: The following are all the possible substrings that meet the
# conditions:
# [
# "adefaddaccc"
# "adefadda",
# "ef",
# "e",
# ⁠ "f",
# "ccc",
# ]
# If we choose the first string, we cannot choose anything else and we'd get
# only 1. If we choose "adefadda", we are left with "ccc" which is the only one
# that doesn't overlap, thus obtaining 2 substrings. Notice also, that it's not
# optimal to choose "ef" since it can be split into two. Therefore, the optimal
# way is to choose ["e","f","ccc"] which gives us 3 substrings. No other
# solution of the same number of substrings exist.
# 
# 
# Example 2:
# 
# 
# Input: s = "abbaccd"
# Output: ["d","bb","cc"]
# Explanation: Notice that while the set of substrings ["d","abba","cc"] also
# has length 3, it's considered incorrect since it has larger total length.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s contains only lowercase English letters.
# 
# 
#

# @lc code=start
from typing import *
class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        
        n = len(s)
        
        prefix_counts = [[0 for _ in range(26)]]
        foo = lambda x: ord(x) - ord('a')
        total =  [0 for _ in range(26)]
        for i, c in enumerate(s):
            new_counts = [0 for _ in range(26)]
            idx = foo(c)
            new_counts[idx] = 1
            total[idx] += 1
            for j, v in enumerate(prefix_counts[-1]):
                new_counts[j] += v
            prefix_counts.append(new_counts)
            # print(new_counts, prefix_counts[-1])


        # print(prefix_counts[-1])
        @cache
        def check_valid(left, right):
            seen = set()
            x = left
            for c in s[left: right+1]:
                idx = foo(c)
                if c in seen:   continue
                seen.add(c)
                right_count = prefix_counts[right + 1][idx]
                left_count = prefix_counts[left + 1][idx]
                if total[idx] - (right_count - left_count + int(left_count == 1 + prefix_counts[left][idx])) != 0:
                    # print(left, right, x, total[idx], left_count, right_count, c, s[left:right + 1])
                    return False
                x += 1
            return True
        all_poss = []
        for start in range(n):
            for end in range(start, n):
                if check_valid(start, end):
                    all_poss.append(s[start:end + 1])
                    print(self.maxNumOfSubstrings(s[end + 1:]))
        
        print(all_poss)
        
# @lc code=end

