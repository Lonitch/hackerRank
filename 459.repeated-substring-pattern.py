#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#
# https://leetcode.com/problems/repeated-substring-pattern/description/
#
# algorithms
# Easy (40.71%)
# Likes:    1039
# Dislikes: 118
# Total Accepted:    99.9K
# Total Submissions: 243.4K
# Testcase Example:  '"abab"'
#
# Given a non-empty string check if it can be constructed by taking a substring
# of it and appending multiple copies of the substring together. You may assume
# the given string consists of lowercase English letters only and its length
# will not exceed 10000.
# 
# 
# 
# Example 1:
# 
# 
# Input: "abab"
# Output: True
# Explanation: It's the substring "ab" twice.
# 
# 
# Example 2:
# 
# 
# Input: "aba"
# Output: False
# 
# 
# Example 3:
# 
# 
# Input: "abcabcabcabc"
# Output: True
# Explanation: It's the substring "abc" four times. (And the substring "abcabc"
# twice.)
# 
# 
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if s=='':
            return False
        n = len(s)
        for l in range(n//2,0,-1):
            pattern = s[:l]*(n//l)
            if pattern==s:
                return True
        return False
            
# @lc code=end

