#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
#
# https://leetcode.com/problems/accounts-merge/description/
#
# algorithms
# Medium (53.48%)
# Likes:    2865
# Dislikes: 510
# Total Accepted:    167.7K
# Total Submissions: 313.6K
# Testcase Example:  '[["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]'
#
# Given a list of accounts where each element accounts[i] is a list of strings,
# where the first element accounts[i][0] is a name, and the rest of the
# elements are emails representing emails of the account.
# 
# Now, we would like to merge these accounts. Two accounts definitely belong to
# the same person if there is some common email to both accounts. Note that
# even if two accounts have the same name, they may belong to different people
# as people could have the same name. A person can have any number of accounts
# initially, but all of their accounts definitely have the same name.
# 
# After merging the accounts, return the accounts in the following format: the
# first element of each account is the name, and the rest of the elements are
# emails in sorted order. The accounts themselves can be returned in any
# order.
# 
# 
# Example 1:
# 
# 
# Input: accounts =
# [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# Output:
# [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# Explanation:
# The first and third John's are the same person as they have the common email
# "johnsmith@mail.com".
# The second John and Mary are different people as none of their email
# addresses are used by other accounts.
# We could return these lists in any order, for example the answer [['Mary',
# 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
# ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']]
# would still be accepted.
# 
# 
# Example 2:
# 
# 
# Input: accounts =
# [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
# Output:
# [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= accounts.length <= 1000
# 2 <= accounts[i].length <= 10
# 1 <= accounts[i][j] <= 30
# accounts[i][0] consists of English letters.
# accounts[i][j] (for j > 0) is a valid email.
# 
# 
#

# @lc code=start
from typing import *
from collections import defaultdict
class DSU:
    def __init__(self) -> None:
        self.parent = list(range(10001))
        self.rank = [1] * 10001
    
    def find(self, x):
        if x != self.parent[x]:
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
            self.parent[y] = x
            self.rank[x] += self.rank[y]
            self.rank[y] = 0

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # dsu = DSU()
        # email_to_name = {}
        # email_to_uniq_id = {}
        # idx = 0
        # for account in accounts:
        #     name = account[0]
        #     for email in account[1:]:
        #         email_to_name[email] = name
        #         if email not in email_to_uniq_id:
        #             email_to_uniq_id[email] = idx
        #             idx += 1
        #         dsu.union(email_to_uniq_id[account[1]], email_to_uniq_id[email])
        # res = defaultdict(list)
        # for email in email_to_name:
        #     # representative node
        #     res[dsu.find(email_to_uniq_id[email])].append(email)
        # return [[email_to_name[v[0]]] + sorted(v) for v in res.values()]
        visited = [0] * len(accounts)
        emails = defaultdict(list)
        res = []
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]
                emails[email].append(i)


        def dfs(i, email_ids):
            if visited[i]:  return
            visited[i] = 1
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                email_ids.add(email)
                for nbr in emails[email]:
                    dfs(nbr, email_ids)
            return email_ids
        for i, account in enumerate(accounts):
            if not visited[i]:
                emails_uniq = dfs(i, set())
                res.append([account[0]] + sorted(emails_uniq))
        return res
        

# @lc code=end

