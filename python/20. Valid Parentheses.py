"""
20. Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

Difficulty: Easy
Companies: Google, Facebook, Microsoft, Amazon, Twitter, Airbnb, Bloomberg

Solution: This is a question to check if you can use stacks (in a reverse order in some sense)
"""

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0 or len(s)%2 !=0:
            return False
        
        stack = []
        dic = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        
        
        for i in s:
            if i in dic.values():
                stack.append(i)
            elif i in dic:
                if not stack or dic[i]!=stack.pop():
                    return False
        return stack == []