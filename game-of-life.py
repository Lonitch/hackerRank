#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#
# https://leetcode.com/problems/game-of-life/description/
#
# algorithms
# Medium (49.26%)
# Likes:    1240
# Dislikes: 226
# Total Accepted:    141.2K
# Total Submissions: 286.2K
# Testcase Example:  '[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]'
#
# According to the Wikipedia's article: "The Game of Life, also known simply as
# Life, is a cellular automaton devised by the British mathematician John
# Horton Conway in 1970."
# 
# Given a board with m by n cells, each cell has an initial state live (1) or
# dead (0). Each cell interacts with its eight neighbors (horizontal, vertical,
# diagonal) using the following four rules (taken from the above Wikipedia
# article):
# 
# 
# Any live cell with fewer than two live neighbors dies, as if caused by
# under-population.
# Any live cell with two or three live neighbors lives on to the next
# generation.
# Any live cell with more than three live neighbors dies, as if by
# over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by
# reproduction.
# 
# 
# Write a function to compute the next state (after one update) of the board
# given its current state. The next state is created by applying the above
# rules simultaneously to every cell in the current state, where births and
# deaths occur simultaneously.
# 
# Example:
# 
# 
# Input: 
# [
# [0,1,0],
# [0,0,1],
# [1,1,1],
# [0,0,0]
# ]
# Output: 
# [
# [0,0,0],
# [1,0,1],
# [0,1,1],
# [0,1,0]
# ]
# 
# 
# Follow up:
# 
# 
# Could you solve it in-place? Remember that the board needs to be updated at
# the same time: You cannot update some cells first and then use their updated
# values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the
# board is infinite, which would cause problems when the active area encroaches
# the border of the array. How would you address these problems?
# 
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def offset(x,y,m,n):
            return [[a,b] for a in range(x-1,x+2) for b in range(y-1,y+2) if 0<=a<m and 0<=b<n]
        
        rule = defaultdict(int,{
            (1,2):1,
            (1,3):1,
            (0,3):1
        })
        m,n=len(board),len(board[0])
        change={}
        for i in range(m):
            for j in range(n):
                nb = sum([board[lb[0]][lb[1]] for lb in offset(i,j,m,n)])-board[i][j]
                if board[i][j]!=rule[(board[i][j],nb)]:
                    change[(i,j)]=rule[(board[i][j],nb)]
        for k,v in change.items():
            board[k[0]][k[1]]=v

# @lc code=end

