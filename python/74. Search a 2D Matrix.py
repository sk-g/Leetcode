# 74. Search a 2D Matrix
# Sanjay Krishna
"""
Write an efficient algorithm that searches for a value in an m x n matrix. 
This matrix has the following properties:

	Integers in each row are sorted from left to right.
	The first integer of each row is greater than the last integer of the previous row.

Example: 
			[
			  [1,   3,  5,  7],
			  [10, 11, 16, 20],
			  [23, 30, 34, 50]
			]

Given target = 3, return true.
"""

# simple idea, if the target is in the 2D matrix,
# it must be in the line (sub Array) such that
# first number of that sub Array < target <= last number of that sub Array
# find the possible array and then do a search in that sub Array

class Solution:
    def binarySearch(self,arr,target):
        l,r = 0, len(arr)-1
        while l<r:
            m = l+(r-l)//2
            if arr[m] == target:
                return True
            elif arr[m] > target:
                r = m
            elif arr[m] < target:
                l = m+1
        return False
    
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        rows = len(matrix)
        columns = len(matrix[0])
        horiz = 0
        #print(rows,columns)
        if columns == 0:
            return False
        #if not matrix:
        #    return False
        if rows == columns == 1:
            return matrix[0][0] == target
        #print(matrix[0][1])
        for i in range(rows):
            if matrix[i][0] == target:
                return True
            elif columns != 0 and matrix[i][0]<target:
                if matrix[i][columns-1] < target:
                    horiz += 1
                    #print("horiz:",horiz)
                elif matrix[i][columns - 1] == target:
                    #print("m[i][c-1]",matrix[i][columns - 1])
                    return True
                else:
                    #print("bin search")
                    return self.binarySearch(matrix[i],target)
        return False
        #print(horiz)