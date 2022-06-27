#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (41.27%)
# Likes:    1248
# Dislikes: 233
# Total Accepted:    361.6K
# Total Submissions: 874.3K
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings, return their sum (also a binary string).
# 
# The input strings are both non-empty and contains only characters 1 or 0.
# 
# Example 1:
# 
# 
# Input: a = "11", b = "1"
# Output: "100"
# 
# Example 2:
# 
# 
# Input: a = "1010", b = "1011"
# Output: "10101"
# 
#

# @lc code=start
class Solution:
    def addBinary(self, s1: str, s2: str) -> str:
        if len(s2)>len(s1):
            a,b=s2,s1
        else:
            a,b=s1,s2
        carry = 0
        ans = ''
        bidx = len(b)-1
        for i in range(len(a)-1,-1,-1):
            if bidx>=0:
                curr=int(b[bidx])+int(a[i])+carry
                ans=str(curr%2)+ans
                carry = curr//2
                bidx-=1
            else:
                curr=int(a[i])+carry
                ans=str(curr%2)+ans
                carry = curr//2
                
        if carry==0:
            return ans
        else:
            return '1'+ans
# @lc code=end

