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
        pattern = ''
        p = 0
        niter = 0
        for c in s:
            if c not in pattern or pattern[p]!=c:
                if niter>0:
                    return False
                else:
                    pattern+=c
                    p=0
            else:
                p+=1
            
            if len(pattern)==p:
                p=0
                niter+=1

        if p==0 and niter>0:
            return True
        else:
            return False
            
# @lc code=end

