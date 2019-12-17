#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#
# https://leetcode.com/problems/find-the-difference/description/
#
# algorithms
# Easy (53.90%)
# Likes:    596
# Dislikes: 251
# Total Accepted:    167.5K
# Total Submissions: 309.9K
# Testcase Example:  '"abcd"\n"abcde"'
#
# 
# Given two strings s and t which consist of only lowercase letters.
# 
# String t is generated by random shuffling string s and then add one more
# letter at a random position.
# 
# Find the letter that was added in t.
# 
# Example:
# 
# Input:
# s = "abcd"
# t = "abcde"
# 
# Output:
# e
# 
# Explanation:
# 'e' is the letter that was added.
# 
#

# @lc code=start
from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if s=='':
            return t
        cts = Counter(s)
        ctt = Counter(t)
        for c in ctt.keys():
            if cts[c]!=ctt[c]:
                return c
# @lc code=end

