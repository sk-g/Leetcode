#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def encode(node):
            if not node:
                res.append("None,")
                return
            res.append(f"{node.val},")
            encode(node.left)
            encode(node.right)
        encode(root)
        return ''.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def decode(deck):
            if deck[0] == 'None':
                deck.popleft()
                return None
            root = TreeNode(int(deck[0]))
            deck.popleft()
            root.left = decode(deck)
            root.right = decode(deck)
            return root
        data = deque(data.split(','))
        root = decode(data)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

