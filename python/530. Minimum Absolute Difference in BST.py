#530. Minimum Absolute Difference in BST.py
"""
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
Note: There are at least two nodes in this BST.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#recursive (dfs)
class Solution:

    def getMinimumDifference(self, root):
        self.prev = None
        self.ans = sys.maxsize
        def search(node):
            if node.left:
                search(node.left)
            if self.prev is not None:
                self.ans = min(self.ans,node.val-self.prev)
            self.prev = node.val
            if node.right:
                search(node.right)
        search(root)
        return self.ans