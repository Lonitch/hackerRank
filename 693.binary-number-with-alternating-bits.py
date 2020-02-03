#
# @lc app=leetcode id=693 lang=python3
#
# [693] Binary Number with Alternating Bits
#
# https://leetcode.com/problems/binary-number-with-alternating-bits/description/
#
# algorithms
# Easy (58.47%)
# Likes:    359
# Dislikes: 74
# Total Accepted:    52.4K
# Total Submissions: 89.1K
# Testcase Example:  '5'
#
# Given a positive integer, check whether it has alternating bits: namely, if
# two adjacent bits will always have different values.
# 
# Example 1:
# 
# Input: 5
# Output: True
# Explanation:
# The binary representation of 5 is: 101
# 
# 
# 
# Example 2:
# 
# Input: 7
# Output: False
# Explanation:
# The binary representation of 7 is: 111.
# 
# 
# 
# Example 3:
# 
# Input: 11
# Output: False
# Explanation:
# The binary representation of 11 is: 1011.
# 
# 
# 
# Example 4:
# 
# Input: 10
# Output: True
# Explanation:
# The binary representation of 10 is: 1010.
# 
# 
#

# @lc code=start
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b = list(bin(n)[2:])
        if len(b)<2:
            return True
        else:
            return b[0]!=b[1] and len(set(b[::2]))==1 and len(set(b[1::2]))==1
        
# @lc code=end

