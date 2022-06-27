#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#
# https://leetcode.com/problems/happy-number/description/
#
# algorithms
# Easy (47.34%)
# Likes:    1197
# Dislikes: 300
# Total Accepted:    295.1K
# Total Submissions: 620.4K
# Testcase Example:  '19'
#
# Write an algorithm to determine if a number is "happy".
# 
# A happy number is a number defined by the following process: Starting with
# any positive integer, replace the number by the sum of the squares of its
# digits, and repeat the process until the number equals 1 (where it will
# stay), or it loops endlessly in a cycle which does not include 1. Those
# numbers for which this process ends in 1 are happy numbers.
# 
# Example: 
# 
# 
# Input: 19
# Output: true
# Explanation: 
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
# 
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        def pdi(n):
            f = 0
            while n>0:
                f+=(n%10)**2
                n=n//10
            return f
        seen = []
        num=n
        while num not in seen and num>1:
            seen.append(num)
            num = pdi(num) 
        return num==1
# @lc code=end

