#
# @lc app=leetcode id=508 lang=python3
#
# [508] Most Frequent Subtree Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import *
from collections import defaultdict

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        sums = defaultdict(int)
        def dfs(node, roll=0):
            nonlocal sums
            if not node:
                return roll
            roll += node.val
            if not node.left and not node.right:
                sums[roll] += 1
                return roll
            if node.left:
                roll += dfs(node.left, 0)
            if node.right:
                roll += dfs(node.right, 0)
            sums[roll] += 1
            return roll
        dfs(root)
        res = []
        max_freq = -float('inf')
        for sum, freq in sums.items():
            max_freq = max(max_freq, freq)
        for sum, freq in sums.items():
            if freq == max_freq:
                res.append(sum)
        return res

# @lc code=end

