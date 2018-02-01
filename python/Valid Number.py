# Valid Number
# https://leetcode.com/problems/valid-number/
# simple pythonic way to catch exception based on float method
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try: 
            a=float (s) 
            return True
        except : return False
        