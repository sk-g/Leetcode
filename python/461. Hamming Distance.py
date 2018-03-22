"""
461. Hamming Distance
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.

idea: xor and then count 1's
"""

# solution 1: count '1'
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x,y = bin(x)[2:],bin(y)[2:]
        res = 0
        x = bin(int(x,2)^int(y,2))[2:]
        for i in x:
            if i == '1':
                res += 1#int(i)
        return res

#solution 2: sum of all digits in the xor of inputs. It basically sums 0s and 1s so.
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x,y = bin(x)[2:],bin(y)[2:]
        res = 0
        x = bin(int(x,2)^int(y,2))[2:]
        for i in x:
            res += int(i)
        return res        