#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#
# https://leetcode.com/problems/word-pattern/description/
#
# algorithms
# Easy (35.86%)
# Likes:    825
# Dislikes: 113
# Total Accepted:    164K
# Total Submissions: 455.9K
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# Given a pattern and a string str, find if str follows the same pattern.
# 
# Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty word in str.
# 
# Example 1:
# 
# 
# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true
# 
# Example 2:
# 
# 
# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false
# 
# Example 3:
# 
# 
# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false
# 
# Example 4:
# 
# 
# Input: pattern = "abba", str = "dog dog dog dog"
# Output: false
# 
# Notes:
# You may assume pattern contains only lowercase letters, and str contains
# lowercase letters that may be separated by a single space.
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def wordPattern(self, pattern: str, str1: str) -> bool:
        if len(pattern)!=len(str1.split()):
            return False
        abmap = defaultdict(str)
        bamap = defaultdict(str)
        for a,b in zip(pattern, str1.split()):
            if abmap[a]=='' and bamap[b]=='':
                abmap[a]=b
                bamap[b]=a
            elif abmap[a]!=b or bamap[b]!=a:
                return False
        return True
# @lc code=end

