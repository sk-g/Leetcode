# 15. 3Sum
# SK
"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]


Binary search with a hack to skip triplets
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        f=[]
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l, h= i+1, len(nums)-1
            while l < h:
                s = nums[i]+nums[l]+nums[h]
                if s<0:
                    l+=1
                elif s>0:
                    h-=1
                else:
                    f.append((nums[i],nums[l],nums[h]))
                    while l<h and nums[l]==nums[l+1]:# check if next number is same, if same, skip it
                        l+=1
                    while l<h and nums[h]==nums[h-1]:# same as above, move pointer accordingly 
                        h-=1
                    l+=1;h-=1
        return f