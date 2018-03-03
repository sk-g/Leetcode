#415. Add Strings
"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

"""
class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        sums = []
        i = len(num1)-1
        j = len(num2)-1
        carry = 0
        while i >= 0 or j >= 0:
            total = carry
            if i >= 0:
                total += int(num1[i])
                i -= 1
            if j >= 0:
                total += int(num2[j])
                j -= 1
            sums.append(str(total % 10))
            carry = total / 10
        if carry:
            sums.append(str(carry))
        
        return "".join(sums[::-1])