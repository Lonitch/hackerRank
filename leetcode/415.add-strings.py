#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#
# https://leetcode.com/problems/add-strings/description/
#
# algorithms
# Easy (45.20%)
# Likes:    580
# Dislikes: 197
# Total Accepted:    129.4K
# Total Submissions: 284.7K
# Testcase Example:  '"0"\n"0"'
#
# Given two non-negative integers num1 and num2 represented as string, return
# the sum of num1 and num2.
# 
# Note:
# 
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to
# integer directly.
# 
# 
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(int(num1)+int(num2))
# @lc code=end

