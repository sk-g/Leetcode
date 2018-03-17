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

## 104 ms, fastest, borrowed + edited for special cases
## using kth order statistics
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        
        nums1 = sorted(nums1+nums2)
        n = len(nums1)-1
        #print(n//2,nums1)
        if n%2 ==0:
            #print(nums1[n//2],nums1[1+n//2])
            
            return nums1[n//2]
        
        return (nums1[n//2]+nums1[1+n//2])/2
        """
        m,n = len(nums1),len(nums2)
        if m ==0 and n == 0:
            return 0.0
        if nums1 == nums2:
            if m%2 != 0:
                return nums1[m//2]
            return (nums1[m//2]+nums1[m//2-1])/2
        if m == 0 and n%2 == 0:
            return (nums2[n//2]+nums2[n//2 - 1])/2
        elif m == 0 and n%2 != 0:
            return nums2[n//2]
        if n == 0 and m%2 == 0:
            return (nums1[m//2]+nums1[m//2 - 1])/2
        elif n == 0 and m%2 != 0:
            return nums1[m//2]            

        m = len(nums1)
        n = len(nums2)
        if (m + n) % 2 == 1:
            return self.findKth(nums1, 0, nums2, 0, (m + n) // 2 + 1)
        return (self.findKth(nums1, 0, nums2, 0, (m + n) // 2) + self.findKth(nums1, 0, nums2, 0, (m + n) // 2 + 1)) / 2.0
    
    def findKth(self, nums1, start1, nums2, start2, k):
        m, n = len(nums1), len(nums2)
        
        if start1 >= m:
            return nums2[start2 + k - 1]
        if start2 >= n:
            return nums1[start1 + k - 1]
        if k == 1:
            return min(nums1[start1], nums2[start2])
        
        if start1 + k // 2 - 1 < m:
            nums1_key = nums1[start1 + k // 2 - 1]
        else:
            nums1_key = sys.maxsize
        
        if start2 + k // 2 - 1 < n:
            nums2_key = nums2[start2 + k // 2 - 1]
        else:
            nums2_key = sys.maxsize
        
        if nums1_key < nums2_key:
            return self.findKth(nums1, start1 + k // 2, nums2, start2, k - k // 2)
        else:
            return self.findKth(nums1, start1, nums2, start2 + k // 2, k - k // 2)            