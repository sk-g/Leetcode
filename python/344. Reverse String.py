"""
344. Reverse String

Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".



obvious pythonic way
"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        # slower more naive approach
        # of swapping
        s=list(s)
        for i in range(len(s)/2):
            t=s[i]
            s[i]=s[len(s)-i-1]
            s[len(s)-i-1]=t
        s = ''.join(s)
        """
            
        return s[::-1]