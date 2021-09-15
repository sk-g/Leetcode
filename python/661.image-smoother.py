#
# @lc app=leetcode id=661 lang=python3
#
# [661] Image Smoother
#

# @lc code=start
from typing import *
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row, col = len(img), len(img[0])
        res =  [[0 for _ in range(col)] for _ in range(row)]
        dirs = [ 
                 [0, 1],
                 [1, 0],
                 [0, -1], 
                 [-1, 0], 
                 [1, 1], 
                 [-1, 1], 
                 [-1, -1], 
                 [1, -1]
                 ]
        for i in range(row):
            for j in range(col):
                temp = [img[i][j]] + [img[x + i][y + j] for x, y in dirs if 0 <= x + i < row and 0 <= y + j < col]
                res[i][j] = sum(temp) // len(temp)
        return res
# @lc code=end

