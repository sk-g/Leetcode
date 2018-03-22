#485. Max Consecutive Ones

"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        max_o = 0
        c = 0
        for i in nums:
            if i == 1:
                c+=1
            else:
                max_o = max(c,max_o)
                c = 0
        return max(c,max_o)