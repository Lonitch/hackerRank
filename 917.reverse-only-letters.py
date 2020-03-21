#
# @lc app=leetcode id=917 lang=python3
#
# [917] Reverse Only Letters
#
# https://leetcode.com/problems/reverse-only-letters/description/
#
# algorithms
# Easy (56.50%)
# Likes:    437
# Dislikes: 31
# Total Accepted:    47.4K
# Total Submissions: 82.9K
# Testcase Example:  '"ab-cd"'
#
# Given a string S, return the "reversed" string where all characters that are
# not a letter stay in the same place, and all letters reverse their
# positions.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: "ab-cd"
# Output: "dc-ba"
# 
# 
# 
# Example 2:
# 
# 
# Input: "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# 
# 
# 
# Example 3:
# 
# 
# Input: "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"
# 
# 
# 
# 
# 
# Note:
# 
# 
# S.length <= 100
# 33 <= S[i].ASCIIcode <= 122 
# S doesn't contain \ or "
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        chars = list(S)
        l,r=0,len(S)-1
        tb = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        cur = ''
        while l<=r:
            if chars[l] in tb and chars[r] in tb:
                chars[l],chars[r]=chars[r],chars[l]
                l+=1
                r-=1
            elif chars[l] in tb:
                r-=1
            elif chars[r] in tb:
                l+=1
            else:
                l+=1
                r-=1
                
        return ''.join(chars)


# @lc code=end

