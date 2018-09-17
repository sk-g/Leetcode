class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        
        res = []
        top = 0
        bottom = len(matrix)-1
        left = 0 
        right = len(matrix[0])-1
        
        while top<=bottom and left<=right:
            #to right
            for i in range(left,right+1):
                res.append(matrix[top][i])
            #to down
            for i in range(top+1,bottom+1):
                res.append(matrix[i][right])
            if left<right and top<bottom:
                #to left
                for i in range(right-1,left,-1):
                    res.append(matrix[bottom][i])
                #to up
                for i in range(bottom,top,-1):
                    res.append(matrix[i][left])
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        return res