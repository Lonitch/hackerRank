#
# @lc app=leetcode id=633 lang=python3
#
# [633] Sum of Square Numbers
#
# https://leetcode.com/problems/sum-of-square-numbers/description/
#
# algorithms
# Easy (32.58%)
# Likes:    415
# Dislikes: 278
# Total Accepted:    56.5K
# Total Submissions: 174K
# Testcase Example:  '5'
#
# Given a non-negative integer c, your task is to decide whether there're two
# integers a and b such that a^2 + b^2 = c.
# 
# Example 1:
# 
# 
# Input: 5
# Output: True
# Explanation: 1 * 1 + 2 * 2 = 5
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: 3
# Output: False
# 
# 
# 
# 
#

# @lc code=start
import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        t = int(math.sqrt(c/2))
        for i in range(t+1):
            f = math.sqrt(c-i**2)
            if int(f)==f:
                return True
        return False
# @lc code=end

