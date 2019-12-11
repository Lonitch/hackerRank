#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (54.18%)
# Likes:    980
# Dislikes: 124
# Total Accepted:    436.6K
# Total Submissions: 802.7K
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t , write a function to determine if t is an anagram
# of s.
# 
# Example 1:
# 
# 
# Input: s = "anagram", t = "nagaram"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "rat", t = "car"
# Output: false
# 
# 
# Note:
# You may assume the string contains only lowercase alphabets.
# 
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your
# solution to such case?
# 
#

# @lc code=start
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        cs = Counter(s)
        ct = Counter(t)
        for i in cs.keys():
            if cs[i]!=ct[i]:
                return False
        return True
        
# @lc code=end

