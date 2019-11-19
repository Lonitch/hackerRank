#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (37.56%)
# Likes:    3628
# Dislikes: 176
# Total Accepted:    757.8K
# Total Submissions: 2M
# Testcase Example:  '"()"'
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# 
# 
# Note that an empty string is also considered valid.
# 
# Example 1:
# 
# 
# Input: "()"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "()[]{}"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: "(]"
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: "([)]"
# Output: false
# 
# 
# Example 5:
# 
# 
# Input: "{[]}"
# Output: true
# 
# 
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if s=="":
            return True
        left=[]
        for a in s:
            if a in ['(','[','{']:
                left.append(a)
            elif not left or abs(ord(a)-ord(left[-1]))>2:
                return False
            else:
                left.pop()
        if len(left)>0:
            return False
        else:
            return True
        
# @lc code=end

