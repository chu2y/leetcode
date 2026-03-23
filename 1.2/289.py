# 根据 百度百科 ， 生命游戏 ，简称为 生命 ，是英国数学家约翰·何顿·康威在 1970 年发明的细胞自动机。
#
# 给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态： 1 即为 活细胞 （live），或 0 即为 死细胞 （dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：
#
# 如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
# 如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
# 如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
# 如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
# 下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是 同时 发生的。给你 m x n 网格面板 board 的当前状态，返回下一个状态。
#
# 给定当前 board 的状态，更新 board 到下一个状态。
#
# 注意 你不需要返回任何东西。
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        step_x = [-1, 0, 1]
        step_y = [-1, 0, 1]
        record = [[board[i][j] for j in range(len(board[i]))] for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                current = board[i][j]
                count_dead = 0
                count_live = 0
                for x in step_x:
                    for y in step_y:
                        if 0 <= x + i < len(board) and 0 <= y + j < len(board[0]):
                            if x == 0 and y == 0:
                                continue
                            elif board[x + i][y + j] == 1:
                                count_live += 1
                            else:
                                count_dead += 1

                if current == 1:
                    if count_live < 2 or count_live > 3:
                        record[i][j] = 0
                    elif count_live == 2 or count_live == 3:
                        record[i][j] = 1
                else:
                    if count_live == 3:
                        record[i][j] = 1
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = record[i][j]
        print(board)


board = [[]]
s = Solution()
s.gameOfLife(board)
