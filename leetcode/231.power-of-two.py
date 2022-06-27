#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#
# https://leetcode.com/problems/power-of-two/description/
#
# algorithms
# Easy (42.53%)
# Likes:    557
# Dislikes: 149
# Total Accepted:    260K
# Total Submissions: 610.4K
# Testcase Example:  '1'
#
# Given an integer, write a function to determine if it is a power of two.
# 
# Example 1:
# 
# 
# Input: 1
# Output: true 
# Explanation: 2^0 = 1
# 
# 
# Example 2:
# 
# 
# Input: 16
# Output: true
# Explanation: 2^4 = 16
# 
# Example 3:
# 
# 
# Input: 218
# Output: false
# 
#

# @lc code=start
from collections import Counter
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<0:
            return False
        else:
            s = Counter(bin(n)[2:])
            return s['1']==1
        
# @lc code=end

