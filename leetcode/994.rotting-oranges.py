#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#
# https://leetcode.com/problems/rotting-oranges/description/
#
# algorithms
# Easy (46.31%)
# Likes:    1103
# Dislikes: 165
# Total Accepted:    67.5K
# Total Submissions: 143.3K
# Testcase Example:  '[[2,1,1],[1,1,0],[0,1,1]]'
#
# In a given grid, each cell can have one of three values:
# 
# 
# the value 0 representing an empty cell;
# the value 1 representing a fresh orange;
# the value 2 representing a rotten orange.
# 
# 
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten
# orange becomes rotten.
# 
# Return the minimum number of minutes that must elapse until no cell has a
# fresh orange.  If this is impossible, return -1 instead.
# 
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# 
# 
# 
# Example 2:
# 
# 
# Input: [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation:  The orange in the bottom left corner (row 2, column 0) is never
# rotten, because rotting only happens 4-directionally.
# 
# 
# 
# Example 3:
# 
# 
# Input: [[0,2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0, the
# answer is just 0.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# grid[i][j] is only 0, 1, or 2.
# 
# 
# 
# 
#

# @lc code=start
from collections import defaultdict, Counter
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        bk = defaultdict(int)
        for i in range(m):
            for j in range(n):
                bk[(i,j)]=grid[i][j]
        ct = Counter(list(bk.values()))
        ans = 0
        if ct[1]==0:
            return 0
        nf,nr = 0,0
        bkk = list(bk.keys())
        while (ct[1]!=nf and ct[2]!=nr) and (ct[1]!=0):
            nf,nr = ct[1],ct[2]
            temp = {}
            for c in bkk:
                x,y = c
                if bk[c]==1:
                    nb=[(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
                    for b in nb:
                        if b in bkk and bk[b]==2:
                            temp[c]=2
            for c in temp.keys():
                bk[c]=temp[c]

            ct = Counter(list(bk.values()))
            ans+=1
        if ct[1]>0:
            return -1
        else:
            return ans

# @lc code=end

