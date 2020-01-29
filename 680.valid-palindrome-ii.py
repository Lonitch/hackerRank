#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#
# https://leetcode.com/problems/valid-palindrome-ii/description/
#
# algorithms
# Easy (35.32%)
# Likes:    1117
# Dislikes: 79
# Total Accepted:    118.6K
# Total Submissions: 332.2K
# Testcase Example:  '"aba"'
#
# 
# Given a non-empty string s, you may delete at most one character.  Judge
# whether you can make it a palindrome.
# 
# 
# Example 1:
# 
# Input: "aba"
# Output: True
# 
# 
# 
# Example 2:
# 
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# 
# 
# 
# Note:
# 
# The string will only contain lowercase characters a-z.
# The maximum length of the string is 50000.
# 
# 
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1
        while l<r:
            if s[l]!=s[r]:
                temp1 = s[l+1:r+1]
                temp2 = s[l:r]
                return temp1==temp1[::-1] or temp2==temp2[::-1]
            l+=1
            r-=1
        return True


        
        

# @lc code=end

