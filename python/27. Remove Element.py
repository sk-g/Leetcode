"""

Given an array and a value, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

Can use set tricks etc but that would take extra space. 
The point of the problem is to do it in place :)
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        p1=0
        p2 =len(nums)-1
        while p1 <= p2:
            if nums[p1] == val:
                nums[p1]=nums[p2]
                nums[p2]=nums[p1] 
                p2-=1
            else:
                p1 +=1
        return p1