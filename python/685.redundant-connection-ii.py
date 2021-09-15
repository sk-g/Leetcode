#
# @lc app=leetcode id=685 lang=python3
#
# [685] Redundant Connection II
#
# https://leetcode.com/problems/redundant-connection-ii/description/
#
# algorithms
# Hard (33.29%)
# Likes:    1291
# Dislikes: 254
# Total Accepted:    46K
# Total Submissions: 138.3K
# Testcase Example:  '[[1,2],[1,3],[2,3]]'
#
# In this problem, a rooted tree is a directed graph such that, there is
# exactly one node (the root) for which all other nodes are descendants of this
# node, plus every node has exactly one parent, except for the root node which
# has no parents.
# 
# The given input is a directed graph that started as a rooted tree with n
# nodes (with distinct values from 1 to n), with one additional directed edge
# added. The added edge has two different vertices chosen from 1 to n, and was
# not an edge that already existed.
# 
# The resulting graph is given as a 2D-array of edges. Each element of edges is
# a pair [ui, vi] that represents a directed edge connecting nodes ui and vi,
# where ui is a parent of child vi.
# 
# Return an edge that can be removed so that the resulting graph is a rooted
# tree of n nodes. If there are multiple answers, return the answer that occurs
# last in the given 2D-array.
# 
# 
# Example 1:
# 
# 
# Input: edges = [[1,2],[1,3],[2,3]]
# Output: [2,3]
# 
# 
# Example 2:
# 
# 
# Input: edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]
# Output: [4,1]
# 
# 
# 
# Constraints:
# 
# 
# n == edges.length
# 3 <= n <= 1000
# edges[i].length == 2
# 1 <= ui, vi <= n
# ui != vi
# 
# 
#

# @lc code=start
from typing import *
import collections

class DSU:
    def __init__(self, n):
        self.parent = {i + 1 : i + 1 for i in range(n)}
        self.rank = {i + 1: 1 for i in range(n)}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] <= self.rank[y]:
            self.rank[y] += self.rank[x]
            self.rank[x] = 0
            self.parent[x] = y
        else:
            self.rank[x] += self.rank[y]
            self.rank[y] = 0
            self.parent[y] = x

class Solution:
    def findRedundantConnection(self, edges: List[List[int]], n=None) -> List[int]:
        if not n:   n = len(edges)
        dsu = DSU(n)
        res = None
        for u, v in edges:
            if dsu.find(u) == dsu.find(v):
                return [u, v]
            else:
                dsu.union(u, v)
        return res

    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        node_with_two_incoming = 0

        indegrees = collections.defaultdict(int)
        for parent, child in edges:
            indegrees[child] += 1
            if indegrees[child] == 2:
                node_with_two_incoming = child
        if not node_with_two_incoming:  return self.findRedundantConnection(edges, n)
        for i in range(len(edges) -1, -1, -1):
            parent, child = edges[i]
            if child == node_with_two_incoming:
                temp_edges = edges[:i] + edges[i + 1:]
                res = self.findRedundantConnection(temp_edges, n)
                if not res:
                    return [parent, child]


        
        
# @lc code=end

