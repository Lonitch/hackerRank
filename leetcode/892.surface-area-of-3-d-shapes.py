#
# @lc app=leetcode id=892 lang=python3
#
# [892] Surface Area of 3D Shapes
#
# https://leetcode.com/problems/surface-area-of-3d-shapes/description/
#
# algorithms
# Easy (57.01%)
# Likes:    209
# Dislikes: 270
# Total Accepted:    15.9K
# Total Submissions: 27.5K
# Testcase Example:  '[[2]]'
#
# On a N * N grid, we place some 1 * 1 * 1 cubes.
# 
# Each value v = grid[i][j] represents a tower of v cubes placed on top of grid
# cell (i, j).
# 
# Return the total surface area of the resulting shapes.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [[2]]
# Output: 10
# 
# 
# 
# Example 2:
# 
# 
# Input: [[1,2],[3,4]]
# Output: 34
# 
# 
# 
# Example 3:
# 
# 
# Input: [[1,0],[0,2]]
# Output: 16
# 
# 
# 
# Example 4:
# 
# 
# Input: [[1,1,1],[1,0,1],[1,1,1]]
# Output: 32
# 
# 
# 
# Example 5:
# 
# 
# Input: [[2,2,2],[2,1,2],[2,2,2]]
# Output: 46
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= N <= 50
# 0 <= grid[i][j] <= 50
# 
# 
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        for i in range(m):
            grid[i]=[0]+grid[i]+[0]
        grid = [[0]*(n+2)]+grid+[[0]*(n+2)]
        ans = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                c=grid[i][j]
                if c>0:
                    ans+=2
                    nb = [c-grid[i][j-1],c-grid[i][j+1],
                    c-grid[i-1][j],c-grid[i+1][j]]
                    for s in nb:
                        if s>0:
                            ans+=s
        return ans

# @lc code=end

