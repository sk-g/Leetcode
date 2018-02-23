# 4. Median of Two Sorted Arrays
# Sanjay Krishna

# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# simple pythonic solution: add the two arrays, sort
# return middle element

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1 += nums2
        nums1.sort()
        if len(nums1)%2 == 0:
            return (nums1[len(nums1)//2 - 1]+nums1[len(nums1)//2])/2
        else:
            return nums1[len(nums1)//2]