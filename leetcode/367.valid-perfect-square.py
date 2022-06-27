#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#
# https://leetcode.com/problems/valid-perfect-square/description/
#
# algorithms
# Easy (40.56%)
# Likes:    565
# Dislikes: 127
# Total Accepted:    135.1K
# Total Submissions: 332.4K
# Testcase Example:  '16'
#
# Given a positive integer num, write a function which returns True if num is a
# perfect square else False.
# 
# Note: Do not use any built-in library function such as sqrt.
# 
# Example 1:
# 
# 
# 
# Input: 16
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: 14
# Output: false
# 
# 
# 
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        f=int(num**0.5)
        return num/f==f
# @lc code=end

