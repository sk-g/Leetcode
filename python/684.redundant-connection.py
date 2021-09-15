#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#
# https://leetcode.com/problems/redundant-connection/description/
#
# algorithms
# Medium (60.17%)
# Likes:    2791
# Dislikes: 272
# Total Accepted:    162.6K
# Total Submissions: 270.3K
# Testcase Example:  '[[1,2],[1,3],[2,3]]'
#
# In this problem, a tree is an undirected graph that is connected and has no
# cycles.
# 
# You are given a graph that started as a tree with n nodes labeled from 1 to
# n, with one additional edge added. The added edge has two different vertices
# chosen from 1 to n, and was not an edge that already existed. The graph is
# represented as an array edges of length n where edges[i] = [ai, bi] indicates
# that there is an edge between nodes ai and bi in the graph.
# 
# Return an edge that can be removed so that the resulting graph is a tree of n
# nodes. If there are multiple answers, return the answer that occurs last in
# the input.
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
# Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
# Output: [1,4]
# 
# 
# 
# Constraints:
# 
# 
# n == edges.length
# 3 <= n <= 1000
# edges[i].length == 2
# 1 <= ai < bi <= edges.length
# ai != bi
# There are no repeated edges.
# The given graph is connected.
# 
# 
#

# @lc code=start
from typing import *

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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dsu = DSU(n)
        res = []
        for u, v in edges:
            if dsu.find(u) == dsu.find(v):
                return [u, v]
            else:
                dsu.union(u, v)

        return res
# @lc code=end

