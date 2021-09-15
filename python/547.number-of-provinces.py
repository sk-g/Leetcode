#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#
# https://leetcode.com/problems/number-of-provinces/description/
#
# algorithms
# Medium (61.79%)
# Likes:    3634
# Dislikes: 202
# Total Accepted:    313.6K
# Total Submissions: 507.5K
# Testcase Example:  '[[1,1,0],[1,1,0],[0,0,1]]'
#
# There are n cities. Some of them are connected, while some are not. If city a
# is connected directly with city b, and city b is connected directly with city
# c, then city a is connected indirectly with city c.
# 
# A province is a group of directly or indirectly connected cities and no other
# cities outside of the group.
# 
# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the
# i^th city and the j^th city are directly connected, and isConnected[i][j] = 0
# otherwise.
# 
# Return the total number of provinces.
# 
# 
# Example 1:
# 
# 
# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 200
# n == isConnected.length
# n == isConnected[i].length
# isConnected[i][j] is 1 or 0.
# isConnected[i][i] == 1
# isConnected[i][j] == isConnected[j][i]
# 
# 
#

# @lc cod=start
from typing import *

class DSU:
    def __init__(self, n):
        self.parent = {i: i for i in range(n)}
        self.rank = {i: 1 for i in range(n)}
    
    def find(self, x):
        if x != self.parent[x]:
            x = self.find(self.parent[x])
        return x

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
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        # Union Find
        # dsu = DSU(n)
        # for i in range(n - 1):
        #     for j in range(i + 1, n):
        #         if dsu.find(i) != dsu.find(j) and isConnected[i][j]:
        #             dsu.union(i, j)
        # return sum([1 for x in dsu.rank.values() if x > 0])

        # dfs
        res = 0
        visited = set()
        def dfs(node):
            for nbr in range(n):
                if isConnected[node][nbr] and nbr not in visited:
                    visited.add(nbr)
                    dfs(nbr)

        for node in range(n):
            if node not in visited:
                res += 1
                dfs(node)
        return res
# @lc code=end

