#687. Longest Univalue Path
"""
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output:

2
Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output:

2
Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.

Use recursion on left, right children if they exist and check if the values are same
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def rec_func(node):
            if not node:
                return 0
            left_len = rec_func(node.left)
            right_len = rec_func(node.right)
            left_stream,right_stream = 0,0
            if node.left and node.left.val == node.val:
                left_stream = left_len+1
            if node.right and node.right.val == node.val:
                right_stream = right_len + 1
            self.ans = max(self.ans,left_stream+right_stream)
            return max(left_stream,right_stream)
        rec_func(root)
        return self.ans