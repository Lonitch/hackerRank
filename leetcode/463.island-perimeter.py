#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#
# https://leetcode.com/problems/island-perimeter/description/
#
# algorithms
# Easy (62.13%)
# Likes:    1346
# Dislikes: 95
# Total Accepted:    159.6K
# Total Submissions: 255.9K
# Testcase Example:  '[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]'
#
# You are given a map in form of a two-dimensional integer grid where 1
# represents land and 0 represents water.
# 
# Grid cells are connected horizontally/vertically (not diagonally). The grid
# is completely surrounded by water, and there is exactly one island (i.e., one
# or more connected land cells).
# 
# The island doesn't have "lakes" (water inside that isn't connected to the
# water around the island). One cell is a square with side length 1. The grid
# is rectangular, width and height don't exceed 100. Determine the perimeter of
# the island.
# 
# 
# 
# Example:
# 
# 
# Input:
# [[0,1,0,0],
# ⁠[1,1,1,0],
# ⁠[0,1,0,0],
# ⁠[1,1,0,0]]
# 
# Output: 16
# 
# Explanation: The perimeter is the 16 yellow stripes in the image below:
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1:
                    ans+=4
                    for a, b in zip([1,-1,0,0],[0,0,1,-1]):
                        if 0<=i+a<m and 0<=j+b<n:
                            ans-=(grid[i+a][j+b]==1)
        return ans
# @lc code=end

