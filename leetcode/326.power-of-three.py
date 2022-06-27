#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#
# https://leetcode.com/problems/power-of-three/description/
#
# algorithms
# Easy (41.87%)
# Likes:    367
# Dislikes: 1244
# Total Accepted:    217.1K
# Total Submissions: 518K
# Testcase Example:  '27'
#
# Given an integer, write a function to determine if it is a power of three.
# 
# Example 1:
# 
# 
# Input: 27
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: 0
# Output: false
# 
# Example 3:
# 
# 
# Input: 9
# Output: true
# 
# Example 4:
# 
# 
# Input: 45
# Output: false
# 
# Follow up:
# Could you do it without using any loop / recursion?
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==0:
            return False
        if n==1:
            return True
            
        while n%3==0:
            n = n//3
        if n==1:
            return True
        else:
            return False
# @lc code=end

