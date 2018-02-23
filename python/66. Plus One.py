# 66. Plus One

"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

solution:
In case the last digit is 9 we have to propagate the carry towards MSB.

instead we can use a hack: convert into single int, add 1, make a list of it and so on

"""

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = int(''.join([str(i) for i in digits]))
        digits += 1
        res = list(str(digits))
        #print(res)
        res = [int(i) for i in res]
        return res