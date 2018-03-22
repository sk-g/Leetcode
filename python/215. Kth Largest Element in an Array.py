#215. Kth Largest Element in an Array

"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.

Simple question to check if you know heaps.

Python has minheap so just -1*array to get max
"""
import heapq
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        
        for num in nums:
            heapq.heappush(heap,-num)
        for i in range(k):
            res = heapq.heappop(heap)
        return -res