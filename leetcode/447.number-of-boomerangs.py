#
# @lc app=leetcode id=447 lang=python3
#
# [447] Number of Boomerangs
#
# https://leetcode.com/problems/number-of-boomerangs/description/
#
# algorithms
# Easy (50.69%)
# Likes:    339
# Dislikes: 537
# Total Accepted:    61.3K
# Total Submissions: 120.5K
# Testcase Example:  '[[0,0],[1,0],[2,0]]'
#
# Given n points in the plane that are all pairwise distinct, a "boomerang" is
# a tuple of points (i, j, k) such that the distance between i and j equals the
# distance between i and k (the order of the tuple matters).
# 
# Find the number of boomerangs. You may assume that n will be at most 500 and
# coordinates of points are all in the range [-10000, 10000] (inclusive).
# 
# Example:
# 
# 
# Input:
# [[0,0],[1,0],[2,0]]
# 
# Output:
# 2
# 
# Explanation:
# The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
# 
# 
# 
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        if  len(points)<3:
            return 0
        n = len(points)
        ansdict = [defaultdict(int) for i in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                d = (points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2
                ansdict[i][int(d)]+=1
                ansdict[j][int(d)]+=1
        ans = 0
        for i in range(n):
            for j in ansdict[i].keys():
                if ansdict[i][j]>=2:
                    ans+=ansdict[i][j]*(ansdict[i][j]-1)
        return ans
# @lc code=end

