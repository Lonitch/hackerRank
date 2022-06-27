#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#
# https://leetcode.com/problems/factorial-trailing-zeroes/description/
#
# algorithms
# Easy (37.63%)
# Likes:    594
# Dislikes: 846
# Total Accepted:    179.3K
# Total Submissions: 476K
# Testcase Example:  '3'
#
# Given an integer n, return the number of trailing zeroes in n!.
# 
# Example 1:
# 
# 
# Input: 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
# 
# Example 2:
# 
# 
# Input: 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.
# 
# Note: Your solution should be in logarithmic time complexity.
# 
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        dv5 = n//5
        if dv5==0:
            return 0
        ans = dv5
        while dv5>0:
            dv5=dv5//5
            ans+=dv5
        return ans

# @lc code=end

