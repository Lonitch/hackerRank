#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#
# https://leetcode.com/problems/sum-of-two-integers/description/
#
# algorithms
# Easy (50.78%)
# Likes:    931
# Dislikes: 1744
# Total Accepted:    157.4K
# Total Submissions: 310.2K
# Testcase Example:  '1\n2'
#
# Calculate the sum of two integers a and b, but you are not allowed to use the
# operator + and -.
# 
# 
# Example 1:
# 
# 
# Input: a = 1, b = 2
# Output: 3
# 
# 
# 
# Example 2:
# 
# 
# Input: a = -2, b = 3
# Output: 1
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        return sum([a,b])
# @lc code=end

