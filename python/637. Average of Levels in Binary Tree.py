"""
637. Average of Levels in Binary Tree

Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
"""

# solution 1: Iterate like building level order traversal, compute rolling average at that level and refresh level

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        ans = []
        level = [root]
        while level:
            s = 0
            for i in level:
                s += i.val
            ave = s/len(level)
            ans.append(ave)
            nlevel = []
            for l in level:
                if l.left:
                    nlevel.append(l.left)
                if l.right:
                    nlevel.append(l.right)
            level = nlevel
        return ans

# solution2: Stephan Pochman way to do it

# use level order traversal and map means at each level.
from statistics import mean
class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        return list(map(mean,self.levelOrder(root)))
    def levelOrder(self, root):# same code for level order traversal #102
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        res = []
        level = [root]
        
        while any(level):
            res.append([node.val for node in level])
            level = [kid for node in level for kid in (node.left,node.right) if kid]
        return res               