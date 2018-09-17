class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # (2n!)/((n+1)!*(n!))
        
        return math.factorial(2*n)//((math.factorial(n+1))*(math.factorial(n)))