#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#
# https://leetcode.com/problems/longest-palindrome/description/
#
# algorithms
# Easy (49.00%)
# Likes:    692
# Dislikes: 68
# Total Accepted:    118.2K
# Total Submissions: 240.4K
# Testcase Example:  '"abccccdd"'
#
# Given a string which consists of lowercase or uppercase letters, find the
# length of the longest palindromes that can be built with those letters.
# 
# This is case sensitive, for example "Aa" is not considered a palindrome
# here.
# 
# Note:
# Assume the length of given string will not exceed 1,010.
# 
# 
# Example: 
# 
# Input:
# "abccccdd"
# 
# Output:
# 7
# 
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
# 
# 
#

# @lc code=start
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        if s=='':
            return 0
        ct = Counter(s)
        ans = 0
        odd = 0
        for c in ct.values():
            if c%2==0:
                ans+=c
            else:
                ans+=c-1
                odd = 1
        return ans+odd

# @lc code=end

