#240. Search a 2D Matrix II
"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.

# same idea as 2D matrix search:
# find the horiz (row) first and then apply 
# bin search in that row

"""

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not target or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        nr,nc = len(matrix)-1,len(matrix[0])-1
        
        i,j = nr,0
        
        for el in range(nr+nc+2):
            if matrix[i][j] == target:
                break
            elif matrix[i][j] < target and j < nc:
                j += 1
            elif matrix[i][j] > target and i > 0:
                i -= 1
        return matrix[i][j] == target