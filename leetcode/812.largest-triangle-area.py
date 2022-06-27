#
# @lc app=leetcode id=812 lang=python3
#
# [812] Largest Triangle Area
#
# https://leetcode.com/problems/largest-triangle-area/description/
#
# algorithms
# Easy (57.03%)
# Likes:    152
# Dislikes: 877
# Total Accepted:    19.1K
# Total Submissions: 33.3K
# Testcase Example:  '[[0,0],[0,1],[1,0],[0,2],[2,0]]'
#
# You have a list of points in the plane. Return the area of the largest
# triangle that can be formed by any 3 of the points.
# 
# 
# Example:
# Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# Output: 2
# Explanation: 
# The five points are show in the figure below. The red triangle is the
# largest.
# 
# 
# 
# 
# Notes: 
# 
# 
# 3 <= points.length <= 50.
# No points will be duplicated.
# -50 <= points[i][j] <= 50.
# Answers within 10^-6 of the true value will be accepted as correct.
# 
# 
# 
# 
#

# @lc code=start
import math
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)
        ans = 0
        for i in range(n-2):
            p1 = points[i]
            for j in range(i+1,n-1):
                p2 = points[j]
                for k in range(j+1,n):
                    p3 = points[k]
                    a = math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
                    b = math.sqrt((p2[0]-p3[0])**2+(p2[1]-p3[1])**2)
                    c = math.sqrt((p1[0]-p3[0])**2+(p1[1]-p3[1])**2)
                    if a+b>c and a+c>b and b+c>a:
                        s = (a+b+c)/2
                        ans = max(ans, math.sqrt(s*(s-a)*(s-b)*(s-c)))
        return ans
# @lc code=end

