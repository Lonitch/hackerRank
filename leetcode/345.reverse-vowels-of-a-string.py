#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#
# https://leetcode.com/problems/reverse-vowels-of-a-string/description/
#
# algorithms
# Easy (42.47%)
# Likes:    488
# Dislikes: 897
# Total Accepted:    183.8K
# Total Submissions: 431.7K
# Testcase Example:  '"hello"'
#
# Write a function that takes a string as input and reverse only the vowels of
# a string.
# 
# Example 1:
# 
# 
# Input: "hello"
# Output: "holle"
# 
# 
# 
# Example 2:
# 
# 
# Input: "leetcode"
# Output: "leotcede"
# 
# 
# Note:
# The vowels does not include the letter "y".
# 
# 
# 
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        if len(s)<=1:
            return s
        vowels = ['a','A','e','E','i','I','o','O','u','U']
        l = 0
        r = len(s)-1
        s = list(s)
        while l<r:
            if s[l] not in vowels:
                l+=1
            if s[r] not in vowels:
                r-=1
            if s[l] in vowels and s[r] in vowels:
                s[l],s[r]=s[r],s[l]
                l+=1
                r-=1
        return ''.join(s)
            
# @lc code=end

