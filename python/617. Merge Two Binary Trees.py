# 617. Merge Two Binary Trees
# work recursively on left child and right child
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 and t2:
            root=TreeNode(t1.val+t2.val)
            root.left=self.mergeTrees(t1.left,t2.left)
            root.right=self.mergeTrees(t2.right,t1.right)
            return root
        return t1 or t2 