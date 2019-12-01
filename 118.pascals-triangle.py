#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
# https://leetcode.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (48.74%)
# Likes:    939
# Dislikes: 85
# Total Accepted:    308.5K
# Total Submissions: 630.6K
# Testcase Example:  '5'
#
# Given a non-negative integer numRows, generate the first numRows of Pascal's
# triangle.
# 
# 
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
# 
# Example:
# 
# 
# Input: 5
# Output:
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
# 
# 
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1],[1,1],[1,2,1]]
        if numRows<=3:
            return ans[:numRows]
        for j in range(3,numRows):
            temp = [ans[-1][i-1]+ans[-1][i] for i in range(1,len(ans[-1]))]
            ans.append([1]+temp+[1])
        return ans
# @lc code=end

