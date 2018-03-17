"""
11. Container With Most Water
DescriptionHintsSubmissionsDiscussSolution
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Difficulty: Medium
Companies: Bloomberg

Solution :
Use two pointer approach starting from both ends and move towards each other.
Idea is that the area is dominated by the base and the shorter line. (in the order of dominance)
So, we start with max base (pointers at opposite end).
We apply dp to check max and current max each time.
"""

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        low,high = 0,len(height)-1
        
        maxArea = 0
        while low<high:
            area = (high-low)*min(height[low],height[high])#computing area
            maxArea = max(maxArea,area)#dp
            if height[low]<height[high]:
                low += 1
            else:
                high-=1
        return maxArea
