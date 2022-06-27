#
# @lc app=leetcode id=504 lang=python3
#
# [504] Base 7
#
# https://leetcode.com/problems/base-7/description/
#
# algorithms
# Easy (45.38%)
# Likes:    185
# Dislikes: 134
# Total Accepted:    48.3K
# Total Submissions: 106.2K
# Testcase Example:  '100'
#
# Given an integer, return its base 7 string representation.
# 
# Example 1:
# 
# Input: 100
# Output: "202"
# 
# 
# 
# Example 2:
# 
# Input: -7
# Output: "-10"
# 
# 
# 
# Note:
# The input will be in range of [-1e7, 1e7].
# 
#

# @lc code=start
import math
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num<0:
            ans = '-'
            num = -num
        else:
            ans = ''
        s = ''
        while num//7>0:
            s+=str(num%7)
            num=num//7

        return ans+(s+str(num))[::-1]
# @lc code=end

