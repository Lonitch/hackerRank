#
# @lc app=leetcode id=840 lang=python3
#
# [840] Magic Squares In Grid
#
# https://leetcode.com/problems/magic-squares-in-grid/description/
#
# algorithms
# Easy (36.30%)
# Likes:    108
# Dislikes: 972
# Total Accepted:    19.4K
# Total Submissions: 53K
# Testcase Example:  '[[4,3,8,4],[9,5,1,9],[2,7,6,2]]'
#
# A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9
# such that each row, column, and both diagonals all have the same sum.
# 
# Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?
# (Each subgrid is contiguous).
# 
# 
# 
# Example 1:
# 
# 
# Input: [[4,3,8,4],
# ⁠       [9,5,1,9],
# ⁠       [2,7,6,2]]
# Output: 1
# Explanation: 
# The following subgrid is a 3 x 3 magic square:
# 438
# 951
# 276
# 
# while this one is not:
# 384
# 519
# 762
# 
# In total, there is only one magic square inside the given grid.
# 
# 
# Note:
# 
# 
# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# 0 <= grid[i][j] <= 15
# 
# 
#

# @lc code=start
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        if m<3 or n<3:
            return 0
        ans=0
        for i in range(m-2):
            for j in range(n-2):
                flat = grid[i][j:j+3]+grid[i+1][j:j+3]+grid[i+2][j:j+3]
                if len(set(flat))==9 and max(flat)==9:
                    r1 = sum(grid[i][j:j+3])
                    r2 = sum(grid[i+1][j:j+3])
                    r3 = sum(grid[i+2][j:j+3])
                    c1 = grid[i][j]+grid[i+1][j]+grid[i+2][j]
                    c2 = grid[i][j+1]+grid[i+1][j+1]+grid[i+2][j+1]
                    c3 = grid[i][j+2]+grid[i+1][j+2]+grid[i+2][j+2]
                    d1 = grid[i][j]+grid[i+1][j+1]+grid[i+2][j+2]
                    d2 = grid[i+2][j]+grid[i+1][j+1]+grid[i][j+2]
                    if len(set([r1,r2,r3,c1,c2,c3,d1,d2]))==1:
                        ans+=1
        return ans
# @lc code=end

