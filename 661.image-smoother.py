#
# @lc app=leetcode id=661 lang=python3
#
# [661] Image Smoother
#
# https://leetcode.com/problems/image-smoother/description/
#
# algorithms
# Easy (49.72%)
# Likes:    215
# Dislikes: 943
# Total Accepted:    42.9K
# Total Submissions: 85.4K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# Given a 2D integer matrix M representing the gray scale of an image, you need
# to design a smoother to make the gray scale of each cell becomes the average
# gray scale (rounding down) of all the 8 surrounding cells and itself.  If a
# cell has less than 8 surrounding cells, then use as many as you can.
# 
# Example 1:
# 
# Input:
# [[1,1,1],
# ⁠[1,0,1],
# ⁠[1,1,1]]
# Output:
# [[0, 0, 0],
# ⁠[0, 0, 0],
# ⁠[0, 0, 0]]
# Explanation:
# For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
# For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
# For the point (1,1): floor(8/9) = floor(0.88888889) = 0
# 
# 
# 
# Note:
# 
# The value in the given matrix is in the range of [0, 255].
# The length and width of the given matrix are in the range of [1, 150].
# 
# 
#

# @lc code=start
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        n = len(M)+2
        m = len(M[0])+2
        N = [[0]*m]
        for i in range(len(M)):
            N.append([0]+M[i]+[0])
        N.append([0]*m)
        ans = []
        for i in range(1,n-1):
            row = []
            if i==1 or i==n-2:
                de = [min(m-2,2)*min(n-2,2)]+[3*min(n-2,2)]*(m-4)+[min(m-2,2)*min(n-2,2)]
            else:
                de = [min(n-2,3)*min(m-2,2)]+[min(m-2,3)*min(n-2,3)]*(m-4)+[min(n-2,3)*min(m-2,2)]
            for j in range(1,m-1):
                cur = N[i][j]+N[i-1][j-1]+N[i-1][j]+N[i-1][j+1]+N[i][j-1]+N[i][j+1]+N[i+1][j+1]+N[i+1][j]+N[i+1][j-1]
                row.append(int(cur/de[j-1]))
            ans.append(row)
        return ans
        
# @lc code=end

