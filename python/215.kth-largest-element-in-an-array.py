#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (60.52%)
# Likes:    6571
# Dislikes: 397
# Total Accepted:    995.4K
# Total Submissions: 1.6M
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Given an integer array nums and an integer k, return the k^th largest element
# in the array.
# 
# Note that it is the k^th largest element in the sorted order, not the k^th
# distinct element.
# 
# 
# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
# 
# 
# Constraints:
# 
# 
# 1 <= k <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# 
# 
#

# @lc code=start
from typing import *
import random
class Solution:
    def findKthLargest(self, arr: List[int], k: int) -> int:
        # (n - k)th order statistic
        def swap(x, y):
            nonlocal arr
            arr[x], arr[y] = arr[y], arr[x]


        def partition(left, right, pivot_index):
            nonlocal arr
            pivot_val = arr[pivot_index]
            swap(right, pivot_index)
            store_index = left
            for i in range(left, right):
                if arr[i] < pivot_val:
                    swap(i, store_index)
                    store_index += 1
            swap(right, store_index)
            return store_index


        def select(left, right, kth_smallest):
            nonlocal arr
            if left == right:   return arr[left]
            idx = random.randint(left, right)
            pivot_index = partition(left, right, idx)
            if pivot_index == kth_smallest: return arr[pivot_index]
            elif pivot_index > kth_smallest:    return select(left, pivot_index - 1, kth_smallest)
            else:   return select(pivot_index + 1, right, kth_smallest)
        
        return select(0, len(arr) - 1, len(arr) - k)


# @lc code=end

