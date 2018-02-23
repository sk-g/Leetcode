#9 Palindrome Number
# simple and straight forward
# only trick in this question
# is to check if the number is divisible
# by 10 so that 100 becomes 1 instead of
# 001 which is not a palindrome
# this also might reduce submission time



class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        g=x # storing number for later use
        if x<0: # handling some end cases as usual
            return False
        elif x<=9:  # single digit case
            return True
        elif x%10==0:   # i
            return False
        elif x==11: # most numbers divisible by 11 are palindrome
                    # but not all, so we can try to handle some cases
            return True
        elif x==111:
            return True
        else:
            a=0 # temporary variable for multiplication
            t=0 # temporary variable to build reverse
            while x:
                t=a*10+x%10
                if t/10!=a:
                    return 0
                a=t
                x=x/10
            
            if a==g:
                
                return True
            else:
                
                return False
                
                