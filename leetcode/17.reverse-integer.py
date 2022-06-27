#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (25.54%)
# Likes:    2594
# Dislikes: 4063
# Total Accepted:    863.9K
# Total Submissions: 3.4M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
# 
# Input: 123
# Output: 321
# 
# 
# Example 2:
# 
# 
# Input: -123
# Output: -321
# 
# 
# Example 3:
# 
# 
# Input: 120
# Output: 21
# 
# 
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
# of this problem, assume that your function returns 0 when the reversed
# integer overflows.
# 
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if not (-2**31<x<2**31-1):
            return 0
        if x<0:
            font=-1
            x=abs(x)
        else:
            font=1
        res = x//10
        cur = x%10
        ans = 0
        while res>0:
            ans=ans*10+cur
            cur = res%10
            res = res//10
        if cur!=0:
            ans=ans*10+cur
        if -2**31<ans<2**31-1:
            return font*ans
        else:
            return 0
        
# @lc code=end

