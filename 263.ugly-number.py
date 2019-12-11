#
# @lc app=leetcode id=263 lang=python3
#
# [263] Ugly Number
#
# https://leetcode.com/problems/ugly-number/description/
#
# algorithms
# Easy (41.05%)
# Likes:    306
# Dislikes: 516
# Total Accepted:    177.7K
# Total Submissions: 432.7K
# Testcase Example:  '6'
#
# Write a program to check whether a given number is an ugly number.
# 
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
# 
# Example 1:
# 
# 
# Input: 6
# Output: true
# Explanation: 6 = 2 × 3
# 
# Example 2:
# 
# 
# Input: 8
# Output: true
# Explanation: 8 = 2 × 2 × 2
# 
# 
# Example 3:
# 
# 
# Input: 14
# Output: false 
# Explanation: 14 is not ugly since it includes another prime factor 7.
# 
# 
# Note:
# 
# 
# 1 is typically treated as an ugly number.
# Input is within the 32-bit signed integer range: [−2^31,  2^31 − 1].
# 
#

# @lc code=start
class Solution:
    def isUgly(self, num: int) -> bool:
        t = num
        if t==1:
            return True
        if t==0:
            return False
        if t%2 and t%3 and t%5:
            return False
        while t%2==0 or t%3==0 or t%5==0:
            if t%2==0:
                t = t//2
            if t%3==0:
                t = t//3
            if t%5==0:
                t = t//5
        if t==1:
            return True
        else:
            return False

# @lc code=end

