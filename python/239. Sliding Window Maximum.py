"""
# 239
 https://leetcode.com/problems/sliding-window-maximum/description/
 Naive n^2 implementations. Check and append maximum from current windiw (temp array here)
 can use heaps to optimize (possibly in one pass)
 python3
 submission details : 
	 Runtime: 1093 ms
	 Runtime: 1052 ms (without accessing temp array)
"""
class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return nums
        left,right = 0,k-1
        #if k == 1:
        #    return [max(nums)]
        res = []
        while right <= len(nums)-1:
            #print(left,right)
            temp = nums[left:right+1] # temporary array for current window
            #print(left,right,temp)
            res.append(max(temp)) # can rewrite it as res.append(max(nums[left:right+1]))
            right += 1
            left += 1
            
        return(res)