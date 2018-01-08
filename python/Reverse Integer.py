#7 Reverse Integer
# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        INT_MAX = 2**31 -1 # for integer overflow
        #INT_MIN = -(2**31 -1)
        if abs(x) < 10:   return x # if the integer is single digit,
        						   # we can just return the same number.
        if x < 0:				   # checking if the number is negative
            r = -int(str(-x)[::-1])# python strings are not mutable, 
            					   # so create a new string with slicing trick
        if x > 0:
            r = int(str(x)[::-1])
        if abs(r) > INT_MAX: #or r < INT_MIN: # check for overflow, using abs() we can
        				 	 # we can skip the extra check for MIN overflow, runs a bit faster
            return 0		 # if overflow occurs after reversing, return 0
        else:
            return r
        """
        if x>=0:
            n = int(str(abs(x))[::-1])
        else:
            n = -int(str(abs(-x))[::-1])
        return n if n.bit_length() < 32 else 0 # same trick but, 
        									   # using inbuilt function to check for overflow
        """