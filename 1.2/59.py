# 给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        count = 0
        result = [[0 for _ in range(n)] for _ in range(n)]
        i = 0
        j = 0
        row = True
        while count < n:
            count += 1
            result[i][j] = count
            if i == 0