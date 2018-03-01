# 373. Find K Pairs with Smallest Sums
"""
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:
Given nums1 = [1,7,11], nums2 = [2,4,6],  k = 3

Return: [1,2],[1,4],[1,6]

The first 3 pairs are returned from the sequence:
[1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:
Given nums1 = [1,1,2], nums2 = [1,2,3],  k = 2

Return: [1,1],[1,1]

The first 2 pairs are returned from the sequence:
[1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:
Given nums1 = [1,2], nums2 = [3],  k = 3 

Return: [1,3],[2,3]

All possible pairs are returned from the sequence:
[1,3],[2,3]

"""

# SOLUTION SOURCE : https://leetcode.com/problems/find-k-pairs-with-smallest-sums/discuss/84550/Slow-1-liner-to-Fast-solutions

####
# IDEA : Use heaps for sum of pairs
####

class Solution(object):

    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        q = []
        def push(i,j):
            if i<len(nums1) and j<len(nums2):
                heapq.heappush(q,[nums1[i]+nums2[j],i,j])
                
        push(0,0) # pushing first sum into heap
        res = []
        while q and len(res) <k:
            print(q,res)
            s,i,j = heapq.heappop(q) #pops out min till here
            res.append([nums1[i],nums2[j]])
            push(i,j+1)
            if j == 0:
                push(i+1,0)
        return res

"""

Sample testcase:

Run Code Status: Finished
×
Run Code Result:
Your input
[1,7,11]
[2,4,6]
3
Your stdout
([[3, 0, 0]], [])
([[5, 0, 1], [9, 1, 0]], [[1, 2]])
([[7, 0, 2], [9, 1, 0]], [[1, 2], [1, 4]])
Your answer
[[1,2],[1,4],[1,6]]
Expected answer
[[1,2],[1,4],[1,6]]



"""        