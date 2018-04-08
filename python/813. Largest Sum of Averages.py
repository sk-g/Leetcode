"""
813. Largest Sum of Averages

We partition a row of numbers A into at most K adjacent (non-empty) groups, then our score is the sum of the average of each group. What is the largest score we can achieve?

Note that our partition must use every number in A, and that scores are not necessarily integers.

Example:
Input: 
A = [9,1,2,3,9]
K = 3
Output: 20
Explanation: 
The best choice is to partition A into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
We could have also partitioned A into [9, 1], [2], [3, 9], for example.
That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.
"""
# 550 ms dp
class Solution:
    def largestSumOfAverages(self, A, K):
        memo = {}
        def search(n, k):
            if (n, k) in memo: return memo[n, k]
            if k == 1:
                memo[n, k] = sum(A[:n]) / float(n)
                return memo[n, k]
            cur, memo[n, k] = 0, 0
            for i in range(n - 1, 0, -1):
                cur += A[i]
                memo[n, k] = max(memo[n, k], search(i, k - 1) + cur / float(n - i))
            return memo[n, k]
        return search(len(A), K)
# 154 ms dp
class Solution:
    def largestSumOfAverages(self, A, K):
        def rec(st, K):
            if (st, K) in cache:
                return cache[(st, K)]
            if K == 1:
                cache[(st, K)] = sum(A[st:])/(len(A)-st)
                return cache[(st, K)]
            total = 0
            res = -math.inf
            for i in range(st, len(A)-K+1):
                total += A[i]
                res = max(res, (total/(i-st+1)) + rec(i+1, K-1))
            cache[(st, K)] = res
            return cache[(st, K)]
        cache = {}
        return rec(0, K)        
# bottom up dp 428 ms no recursion
class Solution(object):
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        l = len(A)
        dp = [[[0 for _ in range(l)] for _ in range(l)] for _ in range(K)]
        for i in range(l):
            sum = 0
            for j in range(i, l):
                sum += A[j]
                dp[0][i][j] = sum / float(j - i + 1)
        
        for k in range(1, K):
            # array ends with i
            for i in range(k, l):
                best = 0
                # best 0 to i with k groups = from 0 to j, k - 1 groups best solution + rest (from j + 1 to i)
                for j in range(k - 1, i):
                    best = max(best, dp[k - 1][0][j] + dp[0][j + 1][i])
                dp[k][0][i] = best
        
        return dp[-1][0][-1]