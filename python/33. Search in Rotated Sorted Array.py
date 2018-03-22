#33. Search in Rotated Sorted Array
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
Solution: binary search with a little trick. Or use pythonic way.
"""
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        
        low,high = 0, len(nums)-1
        
        while low<=high:
            mid = low + (high-low)//2
            
            if target == nums[mid]:
                return mid
            
            elif nums[low] <= nums[mid]:
                if nums[low]<=target<=nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            elif nums[low]>nums[mid]:
                if nums[mid]<=target<=nums[high]:
                    low = mid+1
                else:
                    high = mid-1    
        return -1
# lazy pythonic solution
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        else:
            return nums.index(target)        