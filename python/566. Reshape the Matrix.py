#566. Reshape the Matrix

class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        rows, cols = len(nums),len(nums[0])
        if r*c != rows*cols:
            return nums
        temp = []
        for i in range(rows):
            for j in range(cols):
                temp += nums[i][j],
        res = []
        skip = 0
        for i in range(r):
            x = []
            for j in range(c):
                x += temp[skip*c+j],
            skip += 1
            res += x,
        return res