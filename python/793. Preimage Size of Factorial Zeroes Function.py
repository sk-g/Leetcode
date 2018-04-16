#793. Preimage Size of Factorial Zeroes Function

"""
Let f(x) be the number of zeroes at the end of x!. (Recall that x! = 1 * 2 * 3 * ... * x, and by convention, 0! = 1.)

For example, f(3) = 0 because 3! = 6 has no zeroes at the end, while f(11) = 2 because 11! = 39916800 has 2 zeroes at the end. Given K, find how many non-negative integers x have the property that f(x) = K.

Example 1:
Input: K = 0
Output: 5
Explanation: 0!, 1!, 2!, 3!, and 4! end with K = 0 zeroes.

Example 2:
Input: K = 5
Output: 0
Explanation: There is no x such that x! ends in K = 5 zeroes.
Note:

K will be an integer in the range [0, 10^9]
"""

class Solution:
    def preimageSizeFZF(self, K):
        def nzero(n):
            
            cnt = 0
            while n>0:
                cnt += n // 5
                n = n//5
            return cnt

        if K == 0:
            return 5

        min = 0
        max = K * 5
        while min+1 < max:
            mid = min+(max-min) // 2
            check = nzero(mid)
            if check < K:
                min = mid
            elif check > K:
                max = mid
            else:
                return 5
            

        if nzero(min) == K or nzero(max)==K:
            return 5
        #next = (min // 5 + 1) * 5
        return 0