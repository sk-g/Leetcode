#73. Set Matrix Zeroes
class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if 0 in matrix[0]:
            flag = True
        else:
            flag = False
        for i in range(1,len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0
        for i in range(1,len(matrix)):
            for j in range(len(matrix[0])-1,-1,-1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if flag:
            matrix[0][:] = [0]*len(matrix[0])
                    