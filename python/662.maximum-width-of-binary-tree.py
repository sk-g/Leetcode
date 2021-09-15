#
# @lc app=leetcode id=662 lang=python3
#
# [662] Maximum Width of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
from typing import *

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 1
        current_level_count = 0
        q = deque()
        q.append((root, 0))
        while q:
            new_level = []
            for node, col in q:
                if node.left:
                    new_level.append((node.left, 2 * col))
                if node.right:
                    new_level.append((node.right, 2 * col + 1))
            res = max(res, col  - q[0][1] + 1)
            q = new_level

        return res


# @lc code=end

