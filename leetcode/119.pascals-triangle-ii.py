#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#
# https://leetcode.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (45.89%)
# Likes:    582
# Dislikes: 182
# Total Accepted:    237.3K
# Total Submissions: 515.4K
# Testcase Example:  '3'
#
# Given a non-negative index k where k ≤ 33, return the k^th index row of the
# Pascal's triangle.
# 
# Note that the row index starts from 0.
# 
# 
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
# 
# Example:
# 
# 
# Input: 3
# Output: [1,3,3,1]
# 
# 
# Follow up:
# 
# Could you optimize your algorithm to use only O(k) extra space?
# 
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        elif rowIndex==1:
            return [1,1]
        ans = [1,1]
        for i in range(1,rowIndex):
            ans = [1]+[ans[j-1]+ans[j] for j in range(1,len(ans))]+[1]
        return ans
# @lc code=end

