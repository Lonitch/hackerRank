#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#
# https://leetcode.com/problems/excel-sheet-column-title/description/
#
# algorithms
# Easy (29.83%)
# Likes:    885
# Dislikes: 184
# Total Accepted:    192.2K
# Total Submissions: 643.1K
# Testcase Example:  '1'
#
# Given a positive integer, return its corresponding column title as appear in
# an Excel sheet.
# 
# For example:
# 
# 
# ⁠   1 -> A
# ⁠   2 -> B
# ⁠   3 -> C
# ⁠   ...
# ⁠   26 -> Z
# ⁠   27 -> AA
# ⁠   28 -> AB 
# ⁠   ...
# 
# 
# Example 1:
# 
# 
# Input: 1
# Output: "A"
# 
# 
# Example 2:
# 
# 
# Input: 28
# Output: "AB"
# 
# 
# Example 3:
# 
# 
# Input: 701
# Output: "ZY"
# 
#

# @lc code=start
class Solution:
    def convertToTitle(self, n: int) -> str:
        ans = ''
        cur = n//26
        mod = n%26
        while cur>0:
            if mod==0:
                ans+='Z'
                cur-=1 # Subtle point
            elif mod!=0:
                ans+=chr(64+mod)
            mod = cur%26
            cur = cur//26
        if mod>0:
            ans+=chr(64+mod)

        return ans[::-1]

# @lc code=end

