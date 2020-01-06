#
# @lc app=leetcode id=541 lang=python3
#
# [541] Reverse String II
#
# https://leetcode.com/problems/reverse-string-ii/description/
#
# algorithms
# Easy (46.59%)
# Likes:    324
# Dislikes: 977
# Total Accepted:    74.4K
# Total Submissions: 158.4K
# Testcase Example:  '"abcdefg"\n2'
#
# 
# Given a string and an integer k, you need to reverse the first k characters
# for every 2k characters counting from the start of the string. If there are
# less than k characters left, reverse all of them. If there are less than 2k
# but greater than or equal to k characters, then reverse the first k
# characters and left the other as original.
# 
# 
# Example:
# 
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# 
# 
# 
# Restrictions: 
# 
# ⁠The string consists of lower English letters only.
# ⁠Length of the given string and k will in the range [1, 10000]
# 
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        n=len(s)
        if k<n<2*k:
            return s[:k][::-1]+s[k:]
        elif n<=k:
            return s[::-1]
        i=0
        ans = ''
        while i<n:
            ans+=s[i:i+k][::-1]+s[i+k:i+2*k]
            i+=2*k
            if k<n-i<2*k:
                ans+=s[i:i+k][::-1]+s[i+k:]
                return ans
            elif n-i<=k:
                ans+=s[i:][::-1]
                return ans
        return ans
# @lc code=end

