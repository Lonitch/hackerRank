#
# @lc app=leetcode id=520 lang=python3
#
# [520] Detect Capital
#
# https://leetcode.com/problems/detect-capital/description/
#
# algorithms
# Easy (52.81%)
# Likes:    369
# Dislikes: 230
# Total Accepted:    98.4K
# Total Submissions: 186.1K
# Testcase Example:  '"USA"'
#
# Given a word, you need to judge whether the usage of capitals in it is right
# or not.
# 
# We define the usage of capitals in a word to be right when one of the
# following cases holds:
# 
# 
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# 
# Otherwise, we define that this word doesn't use capitals in a right way.
# 
# 
# 
# Example 1:
# 
# 
# Input: "USA"
# Output: True
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: "FlaG"
# Output: False
# 
# 
# 
# 
# Note: The input will be a non-empty word consisting of uppercase and
# lowercase latin letters.
# 
#

# @lc code=start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        cap = [1 for c in word if 65<=ord(c)<=90]
        if len(cap)==len(word):
            return True
        if not cap:
            return True
        if len(cap)==1 and 65<=ord(word[0])<=90:
            return True
        return False
# @lc code=end

