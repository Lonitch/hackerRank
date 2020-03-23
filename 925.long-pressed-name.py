#
# @lc app=leetcode id=925 lang=python3
#
# [925] Long Pressed Name
#
# https://leetcode.com/problems/long-pressed-name/description/
#
# algorithms
# Easy (44.33%)
# Likes:    440
# Dislikes: 57
# Total Accepted:    32.3K
# Total Submissions: 71.8K
# Testcase Example:  '"alex"\n"aaleex"'
#
# Your friend is typing his name into a keyboard.  Sometimes, when typing a
# character c, the key might get long pressed, and the character will be typed
# 1 or more times.
# 
# You examine the typed characters of the keyboard.  Return True if it is
# possible that it was your friends name, with some characters (possibly none)
# being long pressed.
# 
# 
# 
# Example 1:
# 
# 
# Input: name = "alex", typed = "aaleex"
# Output: true
# Explanation: 'a' and 'e' in 'alex' were long pressed.
# 
# 
# 
# Example 2:
# 
# 
# Input: name = "saeed", typed = "ssaaedd"
# Output: false
# Explanation: 'e' must have been pressed twice, but it wasn't in the typed
# output.
# 
# 
# 
# Example 3:
# 
# 
# Input: name = "leelee", typed = "lleeelee"
# Output: true
# 
# 
# 
# Example 4:
# 
# 
# Input: name = "laiden", typed = "laiden"
# Output: true
# Explanation: It's not necessary to long press any character.
# 
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# name.length <= 1000
# typed.length <= 1000
# The characters of name and typed are lowercase letters.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
#

# @lc code=start
from collections import Counter
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        m,n = len(name),len(typed)
        i,j=0,0
        while i<m:
            c = name[i]
            ct0,ct1=0,0
            while i<m and name[i]==c:
                ct0+=1
                i+=1
            while j<n and typed[j]==c:
                ct1+=1
                j+=1
            if ct1<ct0:
                return False
        return True

            
            
# @lc code=end

