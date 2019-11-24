#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#
# https://leetcode.com/problems/length-of-last-word/description/
#
# algorithms
# Easy (32.34%)
# Likes:    469
# Dislikes: 1950
# Total Accepted:    313.6K
# Total Submissions: 969.4K
# Testcase Example:  '"Hello World"'
#
# Given a string s consists of upper/lower-case alphabets and empty space
# characters ' ', return the length of last word in the string.
# 
# If the last word does not exist, return 0.
# 
# Note: A word is defined as a character sequence consists of non-space
# characters only.
# 
# Example:
# 
# 
# Input: "Hello World"
# Output: 5
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst = s.split()
        if not lst:
            return 0
        else:
            return len(lst[-1])
# @lc code=end

